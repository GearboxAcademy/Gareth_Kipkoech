const btn = document.getElementById('button');
const form = document.getElementById('form')
const myName = document.getElementById('name');
const myEmail = document.getElementById('email');
const message = document.getElementById('message');


document.getElementById('form')
    .addEventListener('submit', function(event) {
        event.preventDefault();

        btn.value = 'Sending...';

        const serviceID = 'service_vhkn1ph';
        const templateID = 'template_6eh7qe9';
        let warning = '';
        if (myName.value.length < 5) {
            myName.style.borderColor = 'red';
            warning += '<br>Your name should be at least 5 characters long';
            btn.value = 'Send Email';
        }
        if (myEmail.value.length < 5) {
            myEmail.style.borderColor = 'red';
            warning += '<br>Enter your correct email';
            btn.value = 'Send Email';
        }
        if (message.value.length < 3) {
            message.style.borderColor = 'red';
            warning += '<br>Message is too short';
            btn.value = 'Send Email';
        }
        if (warning) {
            const div = document.createElement('div');
            div.innerHTML = warning;
            div.style.color = 'red';
            div.style.border = 'none';
            form.prepend(div);
            setTimeout(() => {
                div.remove();
                myName.style.borderColor = '';
                myEmail.style.borderColor = '';
                message.style.borderColor = '';
            }, 5000)
        } else {
            emailjs.sendForm(serviceID, templateID, this)
                .then(() => {
                    btn.value = 'Send Email';
                    alert('Sent!');
                    setTimeout(() => {
                        myName.value = '';
                        myEmail.value = '';
                        message.value = '';
                        console.log('contents cleared.');
                    }, 10000)
                }, (err) => {
                    btn.value = 'Send Email';
                    alert(JSON.stringify(err));
                });
        }

    });