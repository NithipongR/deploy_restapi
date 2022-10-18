const menu = document.querySelector('#menu');
const sidebar = document.querySelector('.sidebar');

window.addEventListener("load",() =>{
    document.querySelector(".loading").classList.add("loader--hidden");
  
    document.querySelector(".loading").addEventListener("transitionend",()=>{
      document.body.removeChild(document.querySelector(".loading"));
    });
  });

menu.addEventListener('click', function () {
    sidebar.classList.toggle('shortly-sidebar');
    if(sidebar.classList.contains('shortly-sidebar')){
        if(window.innerWidth>1365){
        setTimeout('document.querySelector(".table.table-hover.table-bordered.table-sm.nowrap.dataTable.no-footer").style.width ="99.95%";',1);
        setTimeout('document.querySelector(".dataTables_scrollHeadInner").style.width ="99.95%";',1);
        setTimeout('document.querySelector("thead.thead_set").style.width ="99.95%";',1);
            }
    }else{
        // document.querySelector(".table.table-hover.table-bordered.table-sm.nowrap.dataTable.no-footer").style.width ="";
        // document.querySelector(".dataTables_scrollHeadInner").style.width ="";
        // document.querySelector("thead.thead_set").style.width =""
    }
});

