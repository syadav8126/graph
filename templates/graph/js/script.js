const searchWrapper = document.querySelector(".search-input");
const inputBox = document.querySelector("input");
const suggBox = document.querySelector(".autocom-box");

inputBox.onkeyup = (e)=>{
    let userData = e.target.value;
    let emptyArray = [];
    if(userData){
        emptyArray = suggestions.filter((data)=>{
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            return data = '<li>+ data +</li>';
        });
        console.log(emptyArray);
        searchWrapper.classList.add("active");
    }else{

    }
    showSuggestions(emptyArray)
}

function showSuggestions(list){
    let listData;
    if(!list.length){

    }else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}