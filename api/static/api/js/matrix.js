document.addEventListener("DOMContentLoaded", function () {
  let canvas = document.createElement("canvas");
  let ctx = canvas.getContext("2d");
  document.body.appendChild(canvas);

  canvas.style.position = "fixed";
  canvas.style.top = 0;
  canvas.style.left = 0;
  canvas.style.width = "100%";
  canvas.style.height = "100%";
  canvas.style.zIndex = -1;

  let w = (canvas.width = window.innerWidth);
  let h = (canvas.height = window.innerHeight);

  let columns = Math.floor(w / 20);
  let drops = Array(columns).fill(1);

  function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, w, h);

    ctx.fillStyle = "#00ff00";
    ctx.font = "15px Courier New";

    drops.forEach((y, x) => {
      let text = String.fromCharCode(0x30a0 + Math.random() * 96);
      ctx.fillText(text, x * 20, y * 20);

      if (y * 20 > h && Math.random() > 0.975) drops[x] = 0;
      drops[x]++;
    });
  }

  setInterval(draw, 50);
});
