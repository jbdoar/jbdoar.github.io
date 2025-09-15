;; publish.el
(require 'ox-publish)

(defun html-template (contents info)
  (concat (with-temp-buffer
            (insert-file-contents (expand-file-name "template.html" default-directory))
            (buffer-string))
          contents))

(setq org-html-validation-link nil)
(setq org-html-postamble nil)
(setq org-html-head "<style>img { max-width: 600px; }</style>")


(setq org-publish-project-alist
      '(("site-org"
         :base-directory "src"
         :publishing-directory "docs"
         :publishing-function org-html-publish-to-html
         :html-template 'html-template
         :recursive t
	 :exclude ".archive/.*"
	 :with-toc nil
	 :section-numbers nil
	 )))

(org-publish "site-org" t)
