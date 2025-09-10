// docs/javascripts/mathjax.js
window.MathJax = {
  tex: {
    // 为了避免与货币/普通美元符号冲突，推荐关闭 $...$ 行内写法
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    // 块级支持两种：\[...\] 和 $$...$$
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    tags: "none"
  },
  options: {
    // 不在代码块等标签中渲染
    skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"]
  }
};
