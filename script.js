async function addStudent() {

  const student = {
    roll_no: Number(document.getElementById("roll").value),
    name: document.getElementById("name").value,
    department: document.getElementById("dept").value,
    year: Number(document.getElementById("year").value),
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value
  };

  const response = await fetch("http://127.0.0.1:8000/api/students/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(student)
  });

  if (response.ok) {
    alert("Student Saved Successfully!");
  } else {
    alert("Error!");
  }
}