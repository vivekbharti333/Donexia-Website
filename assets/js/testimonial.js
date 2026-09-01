document.addEventListener("DOMContentLoaded", () => {
    const track = document.querySelector(".testimonial-track");
    const slider = document.querySelector(".testimonial-slider");
    const cards = Array.from(document.querySelectorAll(".leader-card"));
    const dotsContainer = document.querySelector(".testimonial-dots");

    if (!track || !slider || !cards.length || !dotsContainer) return;

    let current = 0;
    let interval;
    let pointerId = null;
    let dragStartX = 0;
    let dragDeltaX = 0;
    let isDragging = false;

    function visibleCards() {
        if (window.innerWidth < 768) return 1;
        if (window.innerWidth < 992) return 2;
        return 3;
    }

    function maxIndex() {
        return Math.max(0, cards.length - visibleCards());
    }

    function cardOffset(index) {
        return cards[index].offsetLeft - cards[0].offsetLeft;
    }

    function setTrackPosition(offset, animate = true) {
        track.style.transition = animate ? "" : "none";
        track.style.transform = `translate3d(${-offset}px, 0, 0)`;
    }

    function moveSlider(index, animate = true) {
        current = Math.min(Math.max(index, 0), maxIndex());
        setTrackPosition(cardOffset(current), animate);

        dotsContainer.querySelectorAll("button").forEach((dot, dotIndex) => {
            dot.classList.toggle("active", dotIndex === current);
            dot.setAttribute("aria-current", dotIndex === current ? "true" : "false");
        });
    }

    function rebuildDots() {
        dotsContainer.replaceChildren();
        for (let index = 0; index <= maxIndex(); index += 1) {
            const dot = document.createElement("button");
            dot.type = "button";
            dot.setAttribute("aria-label", `Show testimonial ${index + 1}`);
            dot.classList.toggle("active", index === current);
            dot.addEventListener("click", () => {
                restartAutoSlide();
                moveSlider(index);
            });
            dotsContainer.appendChild(dot);
        }
        moveSlider(Math.min(current, maxIndex()));
    }

    function restartAutoSlide() {
        window.clearInterval(interval);
        interval = window.setInterval(() => {
            moveSlider(current >= maxIndex() ? 0 : current + 1);
        }, 5000);
    }

    function stopAutoSlide() {
        window.clearInterval(interval);
    }

    slider.addEventListener("pointerdown", (event) => {
        if (event.pointerType === "mouse" && event.button !== 0) return;

        pointerId = event.pointerId;
        dragStartX = event.clientX;
        dragDeltaX = 0;
        isDragging = true;
        stopAutoSlide();
        slider.classList.add("is-dragging");
        slider.setPointerCapture(pointerId);
        setTrackPosition(cardOffset(current), false);
    });

    slider.addEventListener("pointermove", (event) => {
        if (!isDragging || event.pointerId !== pointerId) return;

        dragDeltaX = event.clientX - dragStartX;
        const edgeResistance =
            (current === 0 && dragDeltaX > 0) ||
            (current === maxIndex() && dragDeltaX < 0)
                ? 0.28
                : 1;

        setTrackPosition(cardOffset(current) - dragDeltaX * edgeResistance, false);
    });

    function finishDrag(event) {
        if (!isDragging || event.pointerId !== pointerId) return;

        const threshold = Math.min(70, slider.clientWidth * 0.16);
        const direction =
            Math.abs(dragDeltaX) >= threshold ? (dragDeltaX < 0 ? 1 : -1) : 0;

        isDragging = false;
        pointerId = null;
        slider.classList.remove("is-dragging");
        moveSlider(current + direction);
        restartAutoSlide();
    }

    slider.addEventListener("pointerup", finishDrag);
    slider.addEventListener("pointercancel", finishDrag);
    slider.addEventListener("lostpointercapture", (event) => {
        if (isDragging && event.pointerId === pointerId) finishDrag(event);
    });

    slider.addEventListener("mouseenter", stopAutoSlide);
    slider.addEventListener("mouseleave", () => {
        if (!isDragging) restartAutoSlide();
    });

    document.addEventListener("visibilitychange", () => {
        if (document.hidden) {
            stopAutoSlide();
        } else if (!isDragging) {
            restartAutoSlide();
        }
    });

    let resizeTimer;
    window.addEventListener("resize", () => {
        window.clearTimeout(resizeTimer);
        resizeTimer = window.setTimeout(() => {
            rebuildDots();
            moveSlider(current, false);
        }, 150);
    });

    rebuildDots();
    restartAutoSlide();
});
