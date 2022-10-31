
function buildList(data){
    let list = data;
     $(document).ready(function () {
        $('#example').DataTable({
            data: list,
            responsive: true,
            deferRender: true,
            stateSave: true,
            destroy: true,
            scrollX:true,
            order: [[5, 'desc']],
            fixedColumns:   {
              left: 1,
          },
            columnDefs:[
              { targets: 'no-sort', orderable: false },
              {
                 "targets":2,
                 "data":"detail_link",
                 "render": function(data,type,row,meta){
                    if(data == 'Complete'){
                        return '<img src="/static/image/checked.png" style="width: 30px; height: 30px;">'
                    }else{
                        return '<img src="/static/image/cancel.png" style="width: 30px; height: 30px;">'
                    }                  
                 }
               },
              ],
               columns:[
                    {data:'title',width: "20%"},
                    {data:'system',width: "15%"},
                    {data:'docStatus',width: "10%"},
                    {data:'department',width: "10%"},
                    {data:'requesterCode',width: "15%"},
                    {data:'requestDate',width: "15%"},
                    {data:'lastUpdate',width: "15%"},
                ],
                
            });
            
        });

  }

function buildCard(data) {
// console.log("contactsys", data);
let task = document.getElementById("cardshow");
for (let i in data) {
  if(data[i].attachment == "-"){
    var attach = ""
  }else{
    var attach = "( มีเอกสารแนบ )"
  }
  if(data[i].docStatus =="Complete"){
    var status_color = "border-success"
  }else{
    var status_color = "border-danger"
  }
  let item = `
  <div class="card border border-3 my-3 ${status_color}" style="max-width: 500px;">
          <div class="row g-0 pb-0" style="cursor: pointer;" onclick="window.open('${data[i].detailUrl}')">
                <div class="left-card col-2" style="background-color: #027779; border-top-left-radius:2%; border-bottom-left-radius:2%">
                    <img src="${data[i].picturesystem}"
                        class="img-fluid mx-auto my-5 d-block" alt="..."
                        style="width: 45px; height:45px; border-radius:50%;">
                </div>
                <div class="right-card col-10">
                    <div class="card-body" style="padding-bottom: 0px !important;">
                        <div class="card-title h5"><span>${data[i].requesterCode}</span> - <span>${data[i].requesterNameEN}</span></div>
                        <div class="cart-text fw-normal h6"><strong>Department: </strong><span>${data[i].department}&nbsp;${attach}</span></div>
                        <div class="cart-text fw-normal h6"><strong>Title: </strong><span>${data[i].title}</span>
                            <div><small class="text-muted d-flex justify-content-end pt-2">${data[i].requestDate}</small></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
  `;
  task.innerHTML += item;
}
}
