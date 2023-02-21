function get_students() {
    $.ajax({
        url: "/api/attendance",
        type: "GET",
        dataType: "json",
        success: function(data) {
            show_students(data)
        },
        error: function(data) {
            console.log("Error: " + data)
        }
    })
    }
    
    function show_students(student_info) {
            $("#attendancePresent").empty()
            for(student of student_info["students"]) {
                $("#attendancePresent").append(`<li> ${student["name"]} ${student["status"]} </li>`)
            }
    }