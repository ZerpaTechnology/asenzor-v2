	__nest__ (
		__all__,
		'TyniMCE', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'TyniMCE';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var TyniMCE = __class__ ('TyniMCE', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<h5>{}</h5>\n\t\t<textarea>{}</textarea>\n\t\t';
							self.editor = null;
							self.value = '';
							self.source = config.base_url + 'static/js/tinymce/js/tinymce/tinymce.min.js';
							self.sources = list ([config.base_url + 'static/js/tinymce/js/tinymce/jquery.tinymce.min.js']);
							self.styles = list ([]);
							self.content_css = config.base_url + 'static/js/tinymce/js/tinymce/skins/lightgray/content.min.css';
							self.lang = 'es';
							self.theme = 'modern';
							self.fontsize_formats = '9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 18pt 20pt 22pt 24pt';
							self.content = (function __lambda__ (self) {
								return self.target.find ('>textarea');
							});
							self.code_langs = list ([dict ({'text': 'HTML/XML', 'value': 'markup'}), dict ({'text': 'JavaScript', 'value': 'javascript'}), dict ({'text': 'CSS', 'value': 'css'}), dict ({'text': 'PHP', 'value': 'php'}), dict ({'text': 'Ruby', 'value': 'ruby'}), dict ({'text': 'Python', 'value': 'python'}), dict ({'text': 'Java', 'value': 'java'}), dict ({'text': 'C', 'value': 'c'}), dict ({'text': 'C#', 'value': 'csharp'}), dict ({'text': 'C++', 'value': 'cpp'})]);
							self.plugins = list (['advlist autolink link image lists charmap print preview hr anchor pagebreak table', 'searchreplace wordcount visualblocks visualchars fullscreen insertdatetime media nonbreaking emoticons textcolor', 'save table contextmenu directionality emoticons template paste textcolor', 'code codesample']);
							self.toolbar = 'insertfile undo redo preview | fontselect | fontsizeselect | forecolor backcolor emoticons | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | media fullpage code codesample';
							self.font_formats = tuple ([((((((((((((((('Andale Mono=andale mono,times;' + 'Arial=arial,helvetica,sans-serif;') + 'Arial Black=arial black,avant garde;') + 'Book Antiqua=book antiqua,palatino;') + 'Comic Sans MS=comic sans ms,sans-serif;') + 'Courier New=courier new,courier;') + 'Georgia=georgia,palatino;') + 'Helvetica=helvetica;') + 'Impact=impact,chicago;') + 'Symbol=symbol;') + 'Tahoma=tahoma,arial,helvetica,sans-serif;') + 'Terminal=terminal,monaco;') + 'Times New Roman=times new roman,times;') + 'Trebuchet MS=trebuchet ms,geneva;') + 'Verdana=verdana,geneva;') + 'Webdings=webdings;') + 'Wingdings=wingdings,zapf dingbats']);
						});},
						get add () {return __get__ (this, function (self, target) {
							if (self._update) {
								target.py_update ();
								self.content (self).append (target.target);
							}
							else {
								self.children.append (target);
							}
						});},
						get reconectar () {return __get__ (this, function (self) {
							self.editor = self.target.find ('>textarea').tinymce (dict ({'language': self.lang, 'theme': self.theme, 'plugins': self.plugins, 'codesample_languages': self.code_langs, 'content_css': self.content_css, 'fontsize_formats': self.fontsize_formats, 'font_formats': self.font_formats}));
						});},
						get forceSources () {return __get__ (this, function (self) {
							var __iterable0__ = self.sources;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ ('footer').append ("<script src='{}'></script>".format (elem));
							}
						});},
						get forceStyles () {return __get__ (this, function (self) {
							var __iterable0__ = self.styles;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ ('footer').append ("<link rel='stylesheet' href='{}'>".format (elem));
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.value]);
							self.__update__ ();
							if (!__in__ ('tinymce', dir (window))) {
								$ ('footer').append ("<script src='{}'></script>".format (self.source));
								self.forceSources ();
								var cargar = function () {
									self.reconectar ();
								};
								setTimeout (cargar, 2000);
							}
							else {
								self.reconectar ();
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TyniMCE = TyniMCE;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
