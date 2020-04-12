function home(){
    const btncopy = document.querySelector('.btn-copy');
    const alert = document.querySelector('.copy-alert');
    const textresult = document.querySelector('#res-url')

    btncopy.addEventListener('click', () => {
        alert.classList.add('fade-out');
        textresult.select();
        document.execCommand('copy');
        setTimeout(() => {
            alert.classList.remove('fade-out');
        }, 2500);
    })
}