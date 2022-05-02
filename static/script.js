console.log('it working ');

// setting and storing  theme color in local storage
let theme=localStorage.getItem('theme')

if (theme==null){
    setTheme('light')
}
else{
    setTheme(theme)
}
 
// creating click option
let themeDots = document.getElementsByClassName('theme')

for (var i = 0; themeDots.length > i; i++) {
    themeDots[i].addEventListener('click', function () {
        let mode = this.dataset.mode
        console.log('option clicked', mode)
        setTheme(mode)
    })
}

// obtaining theme color from there css
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
   
    // storing theme color from local storage 
    localStorage.setItem('theme',mode)
}


// form validation
function validate() {
      
    if( document.myForm.Name.value == "" ) {
       alert( "Please provide your name!" );
       document.myForm.Name.focus() ;
       return false;
    }
    if( document.myForm.EMail.value == "" ) {
       alert( "Please provide your Email!" );
       document.myForm.EMail.focus() ;
       return false;
    }
    return (true);}
