window.onload = () => {

let inputSearch = document.getElementById('search');
let table = document.getElementById("info");

inputSearch.focus()

inputSearch.addEventListener('keyup',searcher)

function searcher() {
    filter = inputSearch.value.toUpperCase();
    tr = table.getElementsByTagName("tr");

    //Recorriendo Elementos 
    for (let i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByClassName("name-product")[0];
        textValue = td.innerHTML || td.innerText;

        if (textValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}

}