let button=document.querySelectorAll("input[type=button]")
console.log(button)
let écrant=document.getElementById("écrant")
console.log(écrant)
let égal=document.getElementById("e")
console.log(égal)
let opérateurs=["+","-","×","÷","%"]




for(let b=0;b<button.length;b++){
    button[b].addEventListener("click",(event)=>
    {   
        if(event.target.value==="="){
            equation=écrant.value
            let resultat = 0
            let j = 0
            for (i of equation){
                if (opérateurs.includes(i)){
                    if(i==="+"){
                    nombres=equation.split("+")
                    resultat=parseFloat(nombres[0])
                    for (j=1;j<nombres.length;j++){
                        resultat+=parseFloat(nombres[j])
                    }}
                    if(i==="-"){
                        nombres=equation.split("-")
                        resultat=nombres[0]
                        for (j=1;j<nombres.length;j++){
                            resultat-=parseFloat(nombres[j])
                    }}
                    if(i==="÷"){
                        nombres=equation.split("÷")
                        resultat=nombres[0]
                        for (j=1;j<nombres.length;j++){
                            resultat/=parseFloat(nombres[j])
                    }}
                    if(i==="×"){
                        nombres=equation.split("×")
                        resultat=nombres[0]
                        for (j=1;j<nombres.length;j++){
                            resultat*=parseFloat(nombres[j])
                    }}
                    if(i==="%"){
                        nombres=equation.split("%")
                        nombres.pop("")
                        if(nombres[0].includes("×"))
                        {  
                        nombres=nombres[0].split("×")
                        resultat=nombres[0]
                        for (j=1;j<nombres.length;j++){
                            resultat*=parseFloat(nombres[j])
                        }
                        resultat=resultat/100
                    }else{
                        
                        resultat=1
                        for (j=0;j<nombres.length;j++){
                            resultat*=(parseFloat(nombres[j])/100)
                    }}}
                }}
        
                écrant.value= resultat
            
            }else if(event.target.value==="↩"){
                let valeur= ''
            for(let j=0;j<écrant.value.length -1;j++)
                valeur+=écrant.value[j]
            écrant.value=valeur
        }else if(event.target.value==="C"){
            écrant.value=""
        }else{
            écrant.value +=event.target.value
        } 
        
    })

}
écrant.addEventListener("keypress",(event)=>{
    chiffres=["1","2","3","4","5","6","7","8","9","0","."]
    for( i of chiffres){
        if (event.value===i){
          let  chiffre=event.value
            écrant.value+=chiffre
            console.log(typeof(event.value))
        }else{
            écrant.value=chiffre
        }
    }
})   
