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
      bt: "\\boldsymbol{t}"
    }
  },
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
