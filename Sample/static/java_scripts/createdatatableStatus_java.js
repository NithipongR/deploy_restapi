
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
                order: [[4, 'desc']],
                fixedColumns:   {
                  left: 1,
              },
                columnDefs:[
                  { targets: 'no-sort', orderable: false },
                  {
                     "targets":0,
                     "data":"detail_link",
                     "render": function(data,type,row,meta){
                        return'<a href="'+data+'"target="_blank" aria-label="Detail_URL"><img src="/static/image/file.png" style="width: 35px; height: 35px;" alt=""></a>';
                      
                     }
                   },
                  //  {
                  //   'title': 'Action',
                  //   "targets":-1,
                  //    "data":"Approve_btn",
                  //    "render": function(data,type,row,meta){
                  //       return'<button type="button" class="btn bg-success text-light" onclick="changeStatusapprove('+data+')">✔</button><span>   </span><button type="button" class="btn bg-danger text-light" onclick="changeStatusreject('+data+')">✖</button>'; //<img src="/static/image/checkbox.png" style="width: 30px; height: 30px;">
                  //    }
                  //  },

                  //  {
                  //   'title': 'Button',
                  //   "targets":-1,
                  //    "data":"Reject_btn",
                  //    "render": function(data,type,row,meta){
                  //       return'<button type="button" class="btn bg-danger text-light" onclick="changeStatusreject('+data+')">Reject</button>'; //<img src="/static/image/checkbox.png" style="width: 30px; height: 30px;">
                  //    }
                  //  }
                  ],
                   columns:[
                        {data:'detailUrl',width: "5%","className" : "border-start-0"},
                        // {data:'docNumber'},
                        {data:'title',width: "20%"},
                        {data:'department',width: "10%"},
                        {data:'requesterCode',width: "15%"},
                        {data:'requestDate',width: "10%"},
                        // {data:'lastUpdate',width: "7.5%"},
                        {data:'system',width: "10%"},
                        // {data:'docStatus',width: "10%","className": "table-cell-edit"},
                        {data:'attachment',width: "5%"},
                        // {data:'approver'},
                        // {data:'id',width: "15%"},
                        // {data:'id'}
                    ],
                    
                });
                
            });
        // }
            // setTimeout(function() {
            //     location.reload();
            //     }, 10000);
      }

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== "") {
//       const cookies = document.cookie.split(";");
//       for (let i = 0; i < cookies.length; i++) {
//           const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === name + "=") {
//               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//               }
//             }
//           }
//       return cookieValue;
//         }
        
// const csrftoken = getCookie("csrftoken");

// function changeStatusapprove(task){
//   // task = id
//   console.log("Task",task);
//   let status = "Approved";
//   let url = `http://localhost:8000/api/testRequest-update/${task}/`;
//   fetch(url,{
//     method:"POST",
//     headers:{
//       "Content-type" : "application/json",
//       "X-CSRFToken" : csrftoken,
//     },
//     body:JSON.stringify({title:task , docStatus: status}),
//   }).then(function(){
//     // console.log("Yeah!!!")
//     buildList();
//   });
// }

// function changeStatusreject(task){
//   // task = id
//   console.log("Task",task);
//   let status = "Reject";
//   let url = `http://localhost:8000/api/testRequest-update/${task}/`;
//   fetch(url,{
//     method:"POST",
//     headers:{
//       "Content-type" : "application/json",
//       "X-CSRFToken" : csrftoken,
//     },
//     body:JSON.stringify({title:task , docStatus: status}),
//   }).then(function(){
//     // console.log("Yeah!!!")
//     buildList();
//   });
// }
// var table = $('#example').DataTable();
// if(innerWidth<576){
//   $('#example').dataTable().clear();
// }

function buildCard(data) {
  // console.log("contactsys", data);
  let task = document.getElementById("cardshow");
  for (let i in data) {
      // let task_class = "task";
      if(data[i].attachment == "-"){
        // console.log("NO attach")
        var attach = ""
      }else{
        var attach = "( มีเอกสารแนบ )"
      }
      // console.log(data[i].attachment)
      let item = `
      <div class="card border border-3 my-3 border-dark" style="max-width: 500px;">
            <div class="row g-0 pb-0" style="cursor: pointer;" onclick="window.open('${data[i].detailUrl}')">
                <div class="left-card col-2" style="background-color: ${data[i].color}; border-top-left-radius:2%; border-bottom-left-radius:2%">
                    <img src="${data[i].picturesystem}"
                        class="img-fluid mx-auto my-5 d-block" alt="..."
                        style="width: 45px; height:45px; border-radius:50%">
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
