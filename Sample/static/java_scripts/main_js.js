const menu = document.querySelector('#menu');
const sidebar = document.querySelector('.sidebar');

window.addEventListener("load",() =>{
  try{document.querySelector(".loading").classList.add("loader--hidden");
  
    document.querySelector(".loading").addEventListener("transitionend",()=>{
      try{document.body.removeChild(document.querySelector(".loading"));}
      catch(exception){
        
      }
    });}
    catch(exception){
      // console.error("bla");
    }
  });

menu.addEventListener('click', function () {
    sidebar.classList.toggle('shortly-sidebar');
    if(sidebar.classList.contains('shortly-sidebar')){
        if(window.innerWidth>1365){
        setTimeout('document.querySelector(".table.table-hover.table-striped.table-sm.nowrap.dataTable.no-footer").style.width ="100%";',1);
        setTimeout('document.querySelector(".dataTables_scrollHeadInner").style.width ="100%";',1);
        // setTimeout('document.querySelector("thead.thead_set.bg-dark.text-white").style.width ="99.95%";',1);
            }
        if(window.innerWidth<594){
        setTimeout('document.querySelector(".maincon.mx-3.mt-3.bg-white.rounded.w-100").style.opacity ="0.1";',1);
        document.querySelector(".cardshow.container").style.pointerEvents="none";
        // setTimeout('document.querySelector(".card.border.border-3.my-3.border-dark").style.cursor ="none";',1);
        // setTimeout('document.querySelector(".maincon.mx-3.mt-3.bg-white.rounded.w-100").style.visibility ="hidden";',1);
        document.onclick = function(e){
          if(e.target.id == 'maincon')
          {
            sidebar.classList.remove('shortly-sidebar');
            setTimeout('document.querySelector(".maincon.mx-3.mt-3.bg-white.rounded.w-100").style.opacity ="";',1);
            document.querySelector(".cardshow.container").style.pointerEvents="";
            // setTimeout('document.querySelector(".card.border.border-3.my-3.border-dark").style.cursor ="";',1);
            // setTimeout('document.querySelector(".maincon.mx-3.mt-3.bg-white.rounded.w-100").style.visibility ="visible";',1);
          }
        }
        }
    }else{
      setTimeout('document.querySelector(".maincon.mx-3.mt-3.bg-white.rounded.w-100").style.opacity ="";',1);
        // document.querySelector(".table.table-hover.table-striped.table-sm.nowrap.dataTable.no-footer").style.width ="";
        // document.querySelector(".dataTables_scrollHeadInner").style.width ="";
        // document.querySelector("thead.thead_set").style.width =""
    }
});

