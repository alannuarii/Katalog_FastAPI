const result = document.getElementById("result");
const clear = document.getElementById("clear");
const data = document.getElementById("data");

// Fungsi enampilkan value di layar
function display(nilai) {
  result.value += nilai;
  data.value = result.value;
}

// Fungsi menghapus value di layar
if (clear.click) {
  function kosong() {
    result.value = "";
  }
}
