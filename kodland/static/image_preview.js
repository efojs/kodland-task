const fileInput = document.querySelector('input#id_image')
const img = fileInput.files[0]
const src = window.URL.createObjectURL(img)
let imgEl = document.createElement('img')
imgEl.src = src
document.body.append(imgEl)
