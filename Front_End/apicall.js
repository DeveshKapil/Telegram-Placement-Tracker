async function showdata(batch) {
    let x = await fetch("http://127.0.0.1:8000/"+batch);
    let data = await x.json();
    for (let array of data){
        createAdiv(array);
    }
}


createAdiv = (array)=>{
    

    div = document.createElement("div");
    div.className = "show_data";

    batch = document.createElement("p");
    batch.innerHTML  = "Batch: " + array[0];
    batch.style.fontFamily = "Sarah Cadigan-Fried"; // Change font family
    batch.style.fontSize = "20px";    // Change font size
    batch.style.fontWeight = "bold";  // Change font weight
    batch.style.color = "blue";  
    div.append(batch);

    if(array[1]!="N/A"){

        apply = document.createElement("a");
        apply.innerHTML = "Apply link : "+array[1] ;
        apply.style.fontFamily = "Sarah Cadigan-Fried";
        apply.style.fontSize = "20px";
        apply.href = array[1];
        div.append(apply);
    }

    company = document.createElement("p");
    company.innerHTML = "Company " + array[2];
    company.style.fontFamily = "Sarah Cadigan-Fried";
    company.style.fontSize = "20px";
    div.append(company);

    role = document.createElement("p");
    role.innerHTML = "Role: " + array[3];
    role.style.fontFamily = "Sarah Cadigan-Fried";
    role.style.fontSize = "20px";
    div.append(role);

    dis = document.createElement("p");
    dis.innerHTML = "Description: " + array[4]; 
    dis.style.fontFamily = "Sarah Cadigan-Fried";  
    dis.style.fontSize = "18px";
    div.append(dis) ;
    
    var parentDiv = document.getElementById("parent");
    parentDiv.appendChild(div);
    


    // link = document.createElement("a");
    // div.innerHTML =  document.createElement("p");
    // div.innerHTML =  array[1];
    // div.innerHTML =  array[2];
    // link.innerHTML =  "apply here";
    // link.setAttribute("href",array[1]);
    // body.append(div);
    // body.append(link);
}

var aside = document.querySelector("aside");

var batch = aside.id;

showdata(batch);


function log_out(){
    window.location.href = 'logout.php';
}
