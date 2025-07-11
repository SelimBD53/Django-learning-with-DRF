console.log("Student JS loaded");

var SearchQuery = "";
function handle_search(event){
    event.preventDefault(); // Page auto reload korta dai na.
    SearchQuery = document.getElementById('default-search').value;
    handelApi();
}

function handelApi(){
    var url = `/filter-student-api/?search=${SearchQuery}`;
    
    $.ajax({
        url: url,
        type: "GET",
        success: function(data){
            var tableBody = document.getElementById("student_table");
            var new_data = "";
            for (let index=0; index < data.student.length; index++){
                new_data += `
               <tr id="row_${data.student[index].id}" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200">
                    <td>${ data.student[index].username }</td>
                    <td>${ data.student[index].firstname }</td>
                    <td>${ data.student[index].lastname }</td>
                    <td>${ data.student[index].email }</td>
                    <td>${ data.student[index].roll_no }</td>
                    <td>${ data.student[index].dept }</td>
                    <td>${ data.student[index].phone }</td>
                    <td>${ data.student[index].address }</td>
                    ${data.student[index].image ? `
                        <td><img src="${data.student[index].image}" alt="Student Image" class="w-16 h-16 rounded-full"></td>`
                        : ``}       // javascript ar if else condition used system.
                    
                    <td>
                        <a href="/student-data/${data.student[index].id}/" class="text-blue-600 hover:text-blue-900">Edit</a> |
                        <a onclick="deleteStudent(${data.student[index].id})" class="text-red-600 hover:text-red-900">Delete</a>
                    </td>
                </tr>
                `
            }
            tableBody.innerHTML = new_data;
            console.log("Data fetched Successfully", data);
            // windows.location.href=""; // javascript ar khatra full url liktha hoy . data store hobar por kon page a jaba sai ta.
        },
        error: function(xhr, status,error){
            console.log("Error Fetching data:", error);
        }
    });
}