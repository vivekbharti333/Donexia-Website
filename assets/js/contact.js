const API_URL = new URL("/drmapinew/sendContactFormEmail", window.location.origin).href;

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("contact-form");
    const messageDiv = document.getElementById("contactMessage");

    document.querySelectorAll('a[href^="tel:"]').forEach((link) => {
        link.addEventListener("click", () => {
            if (typeof window.gtag === "function") {
                window.gtag("event", "call_click", {
                    location: "contact_page"
                });
            }
        });
    });
    function showMessage(type, heading, message) {
        const alert = document.createElement("div");
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.setAttribute("role", "alert");

        const strong = document.createElement("strong");
        strong.textContent = `${heading} `;
        alert.appendChild(strong);
        alert.appendChild(document.createTextNode(message || ""));

        const closeButton = document.createElement("button");
        closeButton.type = "button";
        closeButton.className = "btn-close";
        closeButton.setAttribute("data-bs-dismiss", "alert");
        closeButton.setAttribute("aria-label", "Close");
        alert.appendChild(closeButton);

        messageDiv.replaceChildren(alert);
    }

    form.addEventListener("submit", async function (e) {

        e.preventDefault();

        messageDiv.innerHTML = "";

        const submitBtn = form.querySelector("button[type='submit']");
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Sending... <i class="bi bi-hourglass-split ms-2"></i>';

        const request = {
            payload: {
                contactName: document.getElementById("fullName").value.trim(),
                emailId: document.getElementById("email").value.trim(),
                mobileNumber: document.getElementById("phone").value.trim(),
                companyName: document.getElementById("organization").value.trim(),
                leadFor: document.getElementById("subject").value,
                notes: document.getElementById("message").value.trim() || document.getElementById("subject").value
            }
        };

        try {

            const response = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(request)
            });

            let result;
            try {
                result = await response.json();
            } catch {
                throw new Error("The server returned an invalid response.");
            }

            if (!response.ok || !result || result.responseCode !== 200 || !result.payload) {
                throw new Error(result?.responseMessage || "Unable to process your request.");
            }

            const payload = result.payload;
            const sent = payload.sendStatus === true ||
                (payload.sendStatus == null && payload.respCode === 200);

                if (sent) {

                    showMessage("success", "Success!", payload.respMesg || "Your message has been sent successfully. Our team will get back to you soon.");
                    if (typeof window.gtag === "function") {
                        window.gtag("event", "generate_lead", {
                            method: "contact_form"
                        });
                    }

                    form.reset();

                } else {

                    showMessage("danger", "Error!", payload.respMesg || "Your message could not be sent. Please try again later or contact us by phone.");
                }

        } catch (error) {

            showMessage("danger", "Error!", error.message || "Something went wrong. Please try again later.");

        } finally {

            submitBtn.disabled = false;
            submitBtn.innerHTML = 'Send Message <i class="bi bi-send ms-2"></i>';

        }

    });

});
