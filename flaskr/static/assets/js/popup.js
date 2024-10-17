function popup(name_inputs, values_inputs, name_buttons, title, url, status) {
    if (status) {
        if (document.querySelector('header') !== null)
            document.querySelector('header').style.display = 'none'
        const box = document.getElementById('box')
        const popupDiv = document.createElement('div')
        popupDiv.className = 'popup'
        if (document.querySelector('nav').style.left === '-280px') {
            popupDiv.style.width = "100vw"
            popupDiv.style.left = "0"
        }
        const popupToggle = document.createElement('div')
        popupToggle.className = 'toggle-popup'
        popupDiv.appendChild(popupToggle)
        const icon = document.createElement('i')
        icon.classList.add('fa-light')
        icon.classList.add('fa-xmark')
        icon.addEventListener('click', () => {
            popup(null,null, false)
        })
        popupToggle.appendChild(icon)
        const form_content = document.createElement('div')
        form_content.className = 'form-content'
        form_content.innerHTML = `
            <div class="container">
                <h4>Teste</h4>
                <hr color="C8CBD9" size="1"/>
                <div id="box">    
                </div>
            </div>
        `;
        popupDiv.appendChild(form_content)
        form_content.querySelector('h4').textContent = title
        box.appendChild(popupDiv)
        form(name_inputs, values_inputs, name_buttons, url, true)
    } else {
        if (document.querySelector('.form-content').querySelector('h4').textContent === "Minha Conta") {
            accountToggle()
        }
        document.querySelector('.popup').remove()
        document.querySelector('header').style.display = 'flex'
    }
}