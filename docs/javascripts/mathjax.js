// MathJax v3 基本配置（在加载 MathJax 主脚本前定义）
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)'], ['$', '$']],
    displayMath: [['\\[', '\\]'], ['$$', '$$']],
    processEscapes: true
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  }
};

// MkDocs Material 的文档内容更新事件：每次“换页”后重新 typeset
// document$ 是 Material 暴露的全局可订阅对象
if (typeof document$ !== 'undefined') {
  document$.subscribe(() => {
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise();  // 关键：重排公式
    }
  });
}
