window.MathJax = {
  tex: {
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    tags: "none",
    macros: {
      argmin: "\\operatorname*{arg\\,min}",
      argmax: "\\operatorname*{arg\\,max}",
      bm: ["\\boldsymbol{#1}", 1],
      bphi: "\\boldsymbol{\\Phi}",
      bt: "\\boldsymbol{t}",
      R: "\\mathbb{R}",
      N: "\\mathbb{N}",
      Z: "\\mathbb{Z}",
      Q: "\\mathbb{Q}",
      C: "\\mathbb{C}",
      E: "\\mathbb{E}"
    }
  },
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
