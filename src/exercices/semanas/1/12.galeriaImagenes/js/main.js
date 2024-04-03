let solution = document.getElementById('solution');
let urlShow = document.getElementById('urlShow');

solution.addEventListener('click', function(){
    if (confirm("¿Estás seguro de desbloquear la solución?") == true) {
        solution.classList.remove('inline-block')
        solution.classList.add('hidde');
        setTimeout(() => {
            urlShow.classList.add('inline-block');
        }, 50);
      }    
});

