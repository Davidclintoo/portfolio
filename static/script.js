console.log('it working ');


let theme=localStorage.getItem('theme')

if (theme=null){
    setTheme('light')
}
else{
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme')

for (var i = 0; themeDots.length > i; i++) {
    themeDots[i].addEventListener('click', function () {
        let mode = this.dataset.mode
        console.log('option clicked', mode)
        setTheme(mode)
    })
}

function setTheme(mode) {
    if (mode == 'light') {
        document.getElementById('light_theme').href = "/static/style.css"
    }

    if (mode == 'blue') {
        document.getElementById('light_theme').href = "/static/blue.css"
    }
    if (mode == 'purple') {
        document.getElementById('light_theme').href = "/static/purple.css"
    }
    if (mode == 'green') {
        document.getElementById('light_theme').href = "/static/green.css"
    }

    localStorage.setItem('theme',mode)
}