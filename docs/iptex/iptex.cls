% IPT Document Class
% 
% --------------------------------------------------------------------------------------
% Tecnologias Regulatórias e Metrológicas
% Área de Aerodinâmica Industrial e Engenharia do Vento - Laboratório de Vazão
%
% Autor: Gabriel Borelli Martins
% E-mail: gborelli@ipt.br
%
% Modelo originariamente baseado no modelo de Relatório Técnico criado para o túnel de 
% vento pelo Pesquisador Paulo Jabardo.
%
% Colaboradores que contribuiram para a elaboração deste modelo:
% Iuri Baldaconi
% Eduardo Katsuno
% Ana Paola Villalva Braga
% André Barsaglini
% --------------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{iptex}[2022/06/03 IPT Document Class]

\DeclareOption{10pt}{\def\@@ptsize{10pt}}
\DeclareOption{11pt}{\def\@@ptsize{11pt}}
\DeclareOption{12pt}{\def\@@ptsize{12pt}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[a4paper,oneside,onecolumn,final,openany,\@@ptsize]{article}

% Incluindo pacotes
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{mathtools}
\RequirePackage{amsmath}
\RequirePackage{amsthm}
\RequirePackage{amsbsy}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{latexsym}
\RequirePackage{mathabx}
\RequirePackage[hidelinks]{hyperref}  
\RequirePackage[pdftex]{graphicx}
\RequirePackage[scaled]{helvet} % Mudar de "helvet" para "uarial" caso fonte arial esteja instalada
\RequirePackage{url}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{indentfirst}
\RequirePackage{color}
\RequirePackage{float}
\RequirePackage{lscape}
\RequirePackage{lastpage}
\RequirePackage[margin=15pt,font=small,labelfont=bf,labelsep=endash,centerlast]{caption}
\RequirePackage{subfig}
\RequirePackage[final]{pdfpages}
\RequirePackage{setspace}
\RequirePackage{changepage}
\RequirePackage[titles,subfigure]{tocloft}
\RequirePackage{ifthen}
\RequirePackage{lipsum} % Apenas para gerar Lorem Ipsum dummy text
\RequirePackage{sectsty}
\RequirePackage{textcomp}
\RequirePackage{booktabs}
\RequirePackage{stmaryrd}
\RequirePackage{siunitx}
\RequirePackage{upgreek} % Para letras gregas não itálicas no texto
\RequirePackage[table]{xcolor}
\RequirePackage{tabularx}
\RequirePackage{enumitem}	
\RequirePackage{geometry}
\RequirePackage{capt-of}
\RequirePackage{xargs}

% Tabelas longas
\RequirePackage{longtable}
\RequirePackage{makecell}


% Página no modo paisagem
\RequirePackage{pdflscape}

% PDF-A
\RequirePackage[a-1b]{pdfx}


% dashed line
\RequirePackage{array}
%\RequirePackage{arydshln}

%	\setlength\dashlinedash{0.2pt}
%	\setlength\dashlinegap{1.5pt}
%	\setlength\arrayrulewidth{1.5pt}
	\setlist{nolistsep}
	\definecolor{green}{HTML}{66FF66}
	\definecolor{myGreen}{HTML}{009900}

	\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
	\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
	\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}

	\renewcommand{\familydefault}{\sfdefault}
	\renewcommand{\arraystretch}{1.5}
	\newdimen\NetTableWidth
  \NetTableWidth=\dimexpr
    \linewidth
    - 8\tabcolsep
    - 5\arrayrulewidth % if package array is loaded
    
			
% Tamanhos de fonte das seções e subseções e alterações no TOC

\sectionfont{\bfseries\large\MakeUppercase}
\renewcommand{\cftsecfont}{\bfseries}
\renewcommand{\cftsecpagefont}{\bfseries}
%\patchcmd{\l@section}{#1}{\MakeUppercase{#1}}{}{} % força seção em maiúsculo no sumário - ruim para flexibilidade de anexos e apendices

\subsectionfont{\bfseries\large}
\renewcommand{\cftsubsecfont}{\bfseries}
\renewcommand{\cftsubsecpagefont}{\bfseries}

\subsubsectionfont{\bfseries\normalsize}
\renewcommand{\cftsubsubsecfont}{\bfseries\normalsize}
\renewcommand{\cftsubsubsecpagefont}{\bfseries}

\setcounter{tocdepth}{4}
\setcounter{secnumdepth}{4}
	
\paragraphfont{\normalsize\normalfont}

\renewcommand\@pnumwidth{3.2em}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}


% Comandos
	\renewcommand{\familydefault}{\sfdefault}
	\renewcommand{\headrulewidth}{0pt}
	\renewcommand{\topfraction}{1}
	\renewcommand{\bottomfraction}{1}
	\renewcommand{\textfraction}{0}
	\renewcommand{\floatpagefraction}{0.8}
	\newcommand{\n}[1]{$\text{#1}$}	

	\newcommand{\docNum}[1]{\gdef\inserirDocNum{#1}}
	\newcommand{\cancelaDoc}[1]{\gdef\inserirCancelaDoc{#1}}
	\newcommand{\cliente}[6]{\gdef\inserirNomeCliente{#1}\gdef\inserirSiglaCliente{#2}
		\gdef\inserirLocalCliente{#3}\gdef\inserirCEPCliente{#4}
		\gdef\inserirCidadeCliente{#5}\gdef\inserirEstadoCliente{#6}}
	\newcommand{\interessado}[5]{\gdef\inserirNomeInt{#1}
		\gdef\inserirLocalInt{#2}\gdef\inserirCEPInt{#3}
		\gdef\inserirCidadeInt{#4}\gdef\inserirEstadoInt{#5}}
	\newcommand{\equip}[1]{\gdef\inserirEquip{#1}}
	\newcommand{\referencia}[1]{\gdef\inserirReferencia{#1}}
	\newcommand{\data}[1]{\gdef\inserirData{#1}}
	\newcommand{\titulo}[1]{\gdef\inserirTitulo{#1}}
	\newcommand{\tipo}[1]{\gdef\inserirTipo{#1}}
	\newcommand{\unidade}[2]{\gdef\inserirUnidade{#1}
		\gdef\inserirUnidadeSigla{#2}}
	\newcommand{\lab}[1]{\gdef\inserirLab{#1}}
	\newcommand{\cabecalhoAcred}[1]{\gdef\inserirCabecalhoAcred{#1}}
	\newcommand{\selo}[1]{\gdef\inserirSelo{#1}}
	\newcommand{\parConfig}[1]{#1}
	\newcommand{\dummylabel}[2]{\def\@currentlabel{#2}\label{#1}} % criando referências "falsas"
	
	\newcommand\firstup[1]{\firstupaux#1\relax}
	\def\firstupaux#1#2\relax{\MakeUppercase{#1}\MakeLowercase{#2}}	%para forçar apenas a primeira letra maiúscula

% Parágrafo

	\setlength{\voffset}{-25.4mm}
	\setlength{\oddsidemargin}{-3.5mm}
	\setlength{\topmargin}{5mm}
	\setlength{\headheight}{28mm}
	\setlength{\headsep}{5mm}
	\setlength{\marginparsep}{0mm}
	\setlength{\textheight}{230mm}
	\setlength{\textwidth}{170mm}
	\setlength{\footskip}{25mm}
	\setlength{\marginparwidth}{0mm}
	
	\def\mypagestyle#1{\csname myps#1\endcsname}

	\newcommand{\mypsCC}{	
		\setlength{\voffset}{-25.4mm}
		\setlength{\oddsidemargin}{-3.5mm}
		\setlength{\topmargin}{5mm}
		\setlength{\headheight}{42mm}
		\setlength{\headsep}{5mm}
		\setlength{\marginparsep}{0mm}
		\setlength{\textheight}{215mm}
		\setlength{\textwidth}{170mm}
		\setlength{\footskip}{25mm}
		\setlength{\marginparwidth}{0mm}
	
	}
	
	
	
	\linespread{1.3} % espaçamento de 1,5 parecido com Word
	%\onehalfspacing % fica com espaçamento menor do que 1,5 do Word
	\setcounter{topnumber}{5}
	\setcounter{bottomnumber}{5}
	\setcounter{totalnumber}{10}
	\setlength{\floatsep}{15pt}
	\setlength{\textfloatsep}{20pt}
	\setlength{\parskip}{6pt}
	\setlength{\parindent}{1.25cm}
	
% Cabeçalhos e rodapé

	\lhead{\includegraphics[scale=0.9]{figuras/headImage.pdf}}
	\chead{}
	\rhead{{\footnotesize \thepage}}
	\lfoot{}
	\cfoot{}
	\rfoot{\includegraphics[scale=1.0]{figuras/footImage.pdf}}
	\pagestyle{fancy}

	\fancypagestyle{geral}{
    		\rhead{{\footnotesize \thepage /\pageref{LastPage}}}
	}

	\fancypagestyle{timbrado}{
		\rhead{}
	}

	\fancypagestyle{tipo_pre}{
		\rhead{\footnotesize \inserirTipo~n\textordmasculine~\inserirDocNum~-~\thepage}
	}

	\fancypagestyle{tipo_doc}{
		\rhead{{\footnotesize \inserirTipo~n\textordmasculine~\inserirDocNum~-~\thepage /\pageref{LastPage}}}
	}



	\fancypagestyle{calibr_pag1}{
		\lhead{\renewcommand{\arraystretch}{1.0}
				\noindent\begin{tabular}{@{}l}
				\includegraphics[scale=0.9]{figuras/headImage.pdf}\\ 
				\footnotesize\textbf{\inserirLab/\inserirUnidade}\\
				\footnotesize\textbf{}
			\end{tabular}
		}
		\rhead{\renewcommand{\arraystretch}{1.3}
				\noindent\begin{tabular}{@{}r}
				\\ 
				  \thepage /\pageref{LastPage} \\
				  \small\textbf{}
			\end{tabular}
		}
		\rfoot{\includegraphics[scale=1.2]{figuras/footImageCalibr.png}}
	}

	\fancypagestyle{calibr_doc}{
		\lhead{\renewcommand{\arraystretch}{1.0}
				\noindent\begin{tabular}{@{}l}
				\includegraphics[scale=0.9]{figuras/headImage.pdf}\\ 
				\footnotesize\textbf{\inserirLab/\inserirUnidade} \\
				\ifdefined\inserirCabecalhoAcred
					\footnotesize\textbf{\inserirCabecalhoAcred}\\
				\else
					\\
				\fi
			\end{tabular}
		}
		\rhead{\renewcommand{\arraystretch}{1.3}
				\noindent\begin{tabular}{@{}r}
				\\
				\thepage /\pageref{LastPage} \\
			 	\footnotesize\textbf{\inserirTipo~n\textordmasculine~\inserirDocNum} 
			\end{tabular}
		}
		\rfoot{\includegraphics[scale=1.2]{figuras/footImageCalibr.png}}
	}

	
% Capa

	\newcommand{\capa}{
	
	\thispagestyle{timbrado}
	
	
	\begin{adjustwidth*}{1.5cm}{1.5cm}
		{\setstretch{1.0}
			\begin{flushright}
				\textbf{\large\MakeUppercase{\inserirTipo}}\\
				
				\ifdefined\inserirDocNum
					\textbf{\large\inserirDocNum}\\
				\fi
	
				
				\ifdefined\inserirSiglaCliente
					\inserirSiglaCliente\\
				\fi			
				
				\inserirData \\
				
				\vspace{3cm}
				
				\inserirTitulo \\
				
				
				\ifdefined\inserirNomeCliente
					\vspace{3cm}
					\textbf{CLIENTE} \\
					\inserirNomeCliente \\
				\fi
				
				\vspace{3cm}
				
				\ifdefined\inserirUnidade
					\textbf{UNIDADE RESPONSÁVEL} \\
					\inserirUnidade ~-- \inserirUnidadeSigla \\
				\fi
				\ifdefined\inserirLab
					\inserirLab \\
				\fi

			\end{flushright}
		}
	\end{adjustwidth*}
	
	\clearpage
}


% Resumo
	\newcommand{\resumo}[3][\textbf{Palavras-chave:}]{
		
		\setcounter{page}{1}
		\renewcommand{\thepage}{\roman{page}}
		
		\section*{RESUMO}
		
		#2
		
		\vspace{0.5cm}
		
		#1 #3
		
		\pagebreak
	}

% Abstract
\newcommand{\resumoeng}[3][\textbf{Keywords:}]{
	
	\setcounter{page}{1}
	\renewcommand{\thepage}{\roman{page}}
	
	\section*{ABSTRACT}
	
	#2
	
	\vspace{0.5cm}
	
	#1 #3
	
	\pagebreak
}


% Página com dados do cliente e título para documentos em geral
	\newcommand{\idCliente}{
		%\thispagestyle{geral}
		%\vspace*{0.5cm}
		\begin{center}
		{\setstretch{0.5}
			\begin{tabular}{c}
				{\large \textbf{\MakeUppercase{\inserirTipo}~N\textordmasculine~\inserirDocNum}} \\
				\ifdefined\inserirCancelaDoc
					Cancela e substitui o~\inserirCancelaDoc
				\fi
			\end{tabular}
		}		
		\end{center}
		\vspace{0.2cm}
		
		{\setstretch{0.5}
		\noindent\begin{tabular}{lp{0.75\textwidth}}
		\ifdefined\inserirTitulo
			\textbf{Título:} & \textbf{\inserirTitulo} \\
			& \\
		\fi
		\textbf{Cliente:} & \textbf{\inserirNomeCliente} \\
			& \textbf{\inserirLocalCliente} \\ 
			& \textbf{CEP \inserirCEPCliente ~-- \inserirCidadeCliente ~-- \inserirEstadoCliente} \\
		\ifdefined\inserirNomeInt
		& \\
		\textbf{Interessado:} & \textbf{\inserirNomeInt} \\
			& \textbf{\inserirLocalInt} \\ 
			& \textbf{\inserirCEPInt ~-- \inserirCidadeInt ~-- \inserirEstadoInt} \\ 
		\fi
		\ifdefined\inserirEquip
		& \\
		\textbf{Item:} & \textbf{\inserirEquip} \\
		\fi
		\ifdefined\inserirReferencia
		& \\
		\textbf{Referência:} & \textbf{\inserirReferencia} \\
		\fi
		
		\end{tabular}
		}
	
	}

% Página com dados do cliente para certificado acreditado
	\newcommand{\idClienteAcred}{
		%\thispagestyle{calibr_pag1}
		%\vspace*{0.1cm}
		\begin{center}
		{\setstretch{0.5}
			\begin{tabular}{c}
				{\large \textbf{\MakeUppercase{\inserirTipo}~N\textordmasculine~\inserirDocNum}} \\
				\ifdefined\inserirCancelaDoc
				Cancela e substitui o~\inserirCancelaDoc
				\fi
			\end{tabular}
		} 
		\end{center}
		
		\ifdefined\inserirEquip
			\vspace{0.2cm}
		\fi
		
		\ifdefined\inserirNomeInt
			\vspace{-1cm}
		\else
			\vspace{-2cm}
		\fi
		
		{\setstretch{0.5}
		\noindent\begin{tabular}{lp{0.6\textwidth}}
		\textbf{Cliente:} & \textbf{\inserirNomeCliente}\\
			& \textbf{\inserirLocalCliente} \\ 
			& \textbf{\inserirCEPCliente ~-- \inserirCidadeCliente ~-- \inserirEstadoCliente}\\		
		\ifdefined\inserirNomeInt
		& \\
		\textbf{Interessado:} & \textbf{\inserirNomeInt}\\
			& \textbf{\inserirLocalInt} \\ 
			& \textbf{\inserirCEPInt ~-- \inserirCidadeInt ~-- \inserirEstadoInt}\\				
		\fi
		\ifdefined\inserirEquip
		& \\
		\textbf{Item:} & \textbf{\inserirEquip} \\
		\fi
		\ifdefined\inserirReferencia
		& \\
		\textbf{Referência:} & \textbf{\inserirReferencia}\\
		\fi
		\end{tabular}}  \hfill  \ifdefined\selo \includegraphics[height=0.15\textheight]{\inserirSelo} \fi
		
		%\vspace{1.0cm}
	}


% Figuras
% 1º parâmetro: posicionamento (opcional)
% 2º parâmetro: nome da imagem com extensão (deve estar na pasta figuras!)
% 3º parâmetro: tamanho (width=\textwidth)
% 4º parâmetro: título (caption)
% 5º parâmetro: rodapé (caption* - fonte)
% 6º parâmetro: chave para referência - deve ser inserida com \label{key}

	\newcommand{\inserirFigura}[6][htb!]{
		\begin{figure}[#1]
			\centering
			\captionsetup{justification=raggedright,
				singlelinecheck=false
			}
			\captionsetup{#3}
			\caption{#4}
			\includegraphics[#3]{./figuras/#2}
			\caption*{#5}
			#6
		\end{figure}	
	}

% Tabelas

% Função de repetição
\makeatletter
\newcount\my@repeat@count
\newcommand{\myrepeat}[2]{%
	\begingroup
	\my@repeat@count=\z@
	\@whilenum\my@repeat@count<#1\do{#2\advance\my@repeat@count\@ne}%
	\endgroup
}
\makeatother

% Tabela curta (modelo para tabelas simples)
% 1º parâmetro: posicionamento (opcional)
% 2º parâmetro: tamanho da fonte (opcional)
% 3º parâmetro: disposição das colunas (ex. l|c|r, para esquerda, centro e direita)
% 4º parâmetro: tamanho do minipage
% 5º parâmetro: conteúdo da tabela
% 6º parâmetro: título (caption)
% 7º parâmetro: rodapé (caption* - fonte)
% 8º parâmetro: chave para referência - deve ser inserida com \label{key}



	\newcommandx{\inserirTabela}[8][1=H, 2=\normalsize]{
		\begin{table}[#1]
			#2
			\centering
			\begin{minipage}{#4} \centering
				\captionsetup{justification=raggedright,
					singlelinecheck=false
				}
				\caption{#6}
				\begin{tabular}{#3}
					#5
				\end{tabular}
				\caption*{#7}
				#8
			\end{minipage}
		\end{table}	

}

% Tabela longa (modelo para tabelas longas simples)
% 1º parâmetro: disposição das colunas (ex. l|c|r, para esquerda, centro e direita)
% 2° parâmetro: número de colunas
% 3º parâmetro: nomes das colunas (separados por &)
% 4º parâmetro: conteúdo da tabela
% 5º parâmetro: título (caption)
% 6º parâmetro: rodapé (caption* - fonte)
% 7º parâmetro: chave para referência - deve ser inserida com \label{key}

	\newcommand{\inserirTabelaLonga}[7]{
		\begin{center}
			\begin{longtable}{#1}
				
				%\caption{#5} \\
				\multicolumn{#2}{l}{\parbox{\LTcapwidth}{\small\singlespacing\textbf{Tabela \thetable} -- #5}} 
				\vspace{0.3cm} \\
				\hline
				#3 \\
				\hline
				\endhead
				
				\hline 
				\multicolumn{#2}{r}{\small\textit{Continua na próxima página}} \\
				\endfoot
				
				\hline
				%\caption*{#6}
				\multicolumn{#2}{l}{\parbox{\LTcapwidth}{\small\singlespacing#6}}
				\endlastfoot
				
				#4
				
				#7
			\end{longtable}
		\end{center}
	}



% Página com assinaturas
%% Três assinaturas digitais
	\newcommand{\assinaturaTresDigital}[6]{
		\begin{flushright}
		\textbf{São Paulo, \inserirData.}
		% Assinaturas
			{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#2} \end{center} & 
				\begin{center} \textbf{#3} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#4} \end{center} \\
				& \begin{center} \textbf{#5} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#6} \end{center}\\ \\
			\end{tabular}
			}
		\end{flushright}
		
		\begin{center}
			\includegraphics[scale=1]{figuras/digital.png}
		\end{center}
		
		\pagebreak
	}

%% Três assinaturas sem identificação de ass. digital
	\newcommand{\assinaturaTres}[6]{
	\begin{flushright}
		\textbf{São Paulo, \inserirData.}
	% Assinaturas
		{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{1.2cm} \textbf{#2} \end{center} &
				\begin{center} \textbf{#3} \\ \vspace{1.2cm} \textbf{#4} \end{center} \\
				& \begin{center} \textbf{#5} \\ \vspace{1.2cm} \textbf{#6} \end{center}\\ \\
			\end{tabular}
		}
	\end{flushright}
	
	\pagebreak
}


%% Três assinaturas digitais - especial p/ certificado acreditado	
	\newcommand{\assinaturaTresAcred}[6]{
		\begin{flushright}
			\textbf{São Paulo, \inserirData.}
		% Assinaturas
			{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#2} \end{center} &
				\begin{center} \textbf{#3} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#4} \end{center} \\
				\begin{center} \textbf{#5} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#6} \end{center}\\ \\
			\end{tabular}
			}
		\end{flushright}
		
		\begin{center}
			\includegraphics[scale=1]{figuras/digital.png}
		\end{center}

		\noindent\textbf{“Este certificado atende aos requisitos de acreditação pela Cgcre, que avaliou a competência do laboratório e 		comprovou sua rastreabilidade a padrões nacionais de medida (ou ao Sistema Internacional de Unidades – SI).”}		
		
		\pagebreak
	}
	
%% Duas assinaturas digitais
	\newcommand{\assinaturaDoisDigital}[4]{
		\begin{flushright}
			\textbf{São Paulo, \inserirData.}
		% Assinaturas
			{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#2} \end{center} & 
				\begin{center} \textbf{#3} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#4} \end{center}\\ \\
			\end{tabular}
			}
		\end{flushright}
				
		\begin{center}	
			\includegraphics[scale=1]{figuras/digital.png}
		\end{center}	
		
		\pagebreak
	}


%% Duas assinaturas sem identificação de ass. digital
	\newcommand{\assinaturaDois}[4]{
	\begin{flushright}
		\textbf{São Paulo, \inserirData.}
	% Assinaturas
		{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{0.8cm} \textbf{#2} \end{center} &
				\begin{center} \textbf{#3} \\ \vspace{0.8cm} \textbf{#4} \end{center}\\ \\
			\end{tabular}
		}
	\end{flushright}
	
	\pagebreak
}


%% Duas assinaturas digitais - especial p/ certificado acreditado
	\newcommand{\assinaturaDoisAcred}[4]{
		\begin{flushright}
			\textbf{São Paulo, \inserirData.}
		% Assinaturas
			{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#2} \end{center} &
				\begin{center} \textbf{#3} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\\textbf{#4} \end{center}\\ \\
			\end{tabular}
			}
		\end{flushright}
		
		\begin{center}
			\includegraphics[scale=1]{figuras/digital.png}
		\end{center}

		\noindent\textbf{“Este certificado atende aos requisitos de acreditação pela Cgcre, que avaliou a competência do laboratório e 		comprovou sua rastreabilidade a padrões nacionais de medida (ou ao Sistema Internacional de Unidades – SI).”}		
		
		\pagebreak
	}
		

%% Uma assinatura digital
	\newcommand{\assinaturaUmDigital}[2]{
		\begin{flushright}
			\textbf{São Paulo, \inserirData.}
		% Assinaturas
			{\scriptsize\singlespacing
				\begin{tabular}{p{8cm}}
					\begin{center} \textbf{#1} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#2} \end{center} \\
				\end{tabular}
			}
		\end{flushright}
		
		\begin{center}
			\includegraphics[scale=1]{figuras/digital.png}
		\end{center}
		
		\pagebreak
	}
	

%% Uma assinatura sem identificação de ass. digital
\newcommand{\assinaturaUm}[2]{
	\begin{flushright}
		\textbf{São Paulo, \inserirData.}
	% Assinaturas
		{\scriptsize\singlespacing
			\begin{tabular}{p{8cm}}
				\begin{center} \textbf{#1} \\ \vspace{0.8cm} \textbf{#2} \end{center} \\
			\end{tabular}
		}
	\end{flushright}
	
	\pagebreak
}



%% Uma assinatura - especial p/ certificado acreditado
	\newcommand{\assinaturaUmAcred}[2]{
		\begin{flushright}
			\textbf{São Paulo, \inserirData.}
		% Assinaturas
			{\scriptsize\singlespacing
				\begin{tabular}{p{8cm}}
					\begin{center} \textbf{#1} \\ \vspace{0.2cm} {\color{blue} Assinado Digitalmente} \vspace{0.2cm} \\ \textbf{#2} \end{center} \\
				\end{tabular}
			}
		\end{flushright}
		
		\begin{center}
			\includegraphics[scale=1]{figuras/digital.png}
		\end{center}
		
		\noindent\textbf{“Este certificado atende aos requisitos de acreditação pela Cgcre, que avaliou a competência do laboratório e 		comprovou sua rastreabilidade a padrões nacionais de medida (ou ao Sistema Internacional de Unidades – SI).”}		
		
		\pagebreak
	}
		
%% Bibliografia
%
%	\newcommand{\bibliografia}[1]{
%		
%		\renewcommand{\refname}{Bibliografia}
%		\addcontentsline{toc}{section}{Referências}
%		\bibliography{#1}	
%	}

% Apêndices
% Apêndice de Relatório Técnico
% 1º parâmetro: identificação do apêndice (A, B, C, ...)
% 2° parâmetro: nome do apêndice
% 3º parâmetro: label do apêndice
\newcommand{\apendice}[4]{
	
	\dummylabel{#3}{#1}

	\addcontentsline{toc}{section}{APÊNDICE #1 - #2}
	\section*{APÊNDICE #1 - \MakeUppercase{#2}}
	
	\renewcommand{\thefigure}{#1.\arabic{figure}}
	\renewcommand{\thetable}{#1.\arabic{table}}
	\setcounter{figure}{0}
	\setcounter{table}{0}
}

% Anexos 
% Anexo de Relatório Técnico, com folha de rosto
% 1º parâmetro: identificação do anexo (A, B, C, ...)
% 2° parâmetro: nome do anexo
% 3º parâmetro: label do anexo
% 4º parâmetro: número total de páginas do anexo.
	\newcommand{\anexo}[4]{
	
	\dummylabel{#3}{#1}
	
	\fancypagestyle{anexo}{
		\rhead{{\footnotesize Anexo #1 do \inserirTipo~n\textordmasculine~\inserirDocNum~-~\thepage /\pageref{LastPage}}}
	}
	
	\pagestyle{anexo}
		
	\vspace*{5cm}
	\begin{center}
		
		\cftaddtitleline{toc}{section}{ANEXO #1 - #2}{#4 pág.}
		%\addcontentsline{toc}{section}{ANEXO #1 - #2}
		
		\large\textbf{ANEXO #1}
		
		
		\vspace{4cm}
		
		\large\bfseries\MakeUppercase{#2}
		
	\end{center}
	
	
	\pagebreak
	
	
		
%	\renewcommand{\thefigure}{#1.\arabic{figure}}
%	\renewcommand{\thetable}{#1.\arabic{table}}
%	\setcounter{figure}{0}
%	\setcounter{table}{0}
	}

% Anexo de Certificado de Calibração, sem folha de rosto
% 1º parâmetro: identificação do anexo (A, B, C, ...)
% 2° parâmetro: nome do anexo
% 3º parâmetro: label do anexo
	\newcommand{\anexoSemFolhaRosto}[3]{
	
	\dummylabel{#3}{#1}
	
	\fancypagestyle{anexo_sfr}{
		\lhead{\renewcommand{\arraystretch}{1.0}
				\noindent\begin{tabular}{@{}l}
				\includegraphics[scale=0.9]{figuras/headImage.pdf}\\ 
				\footnotesize\textbf{\inserirLab/\inserirUnidade} \\
				\ifdefined\inserirCabecalhoAcred
					\footnotesize\textbf{\inserirCabecalhoAcred}\\
				\else
					\\
				\fi
			\end{tabular}
		}
		\rhead{\renewcommand{\arraystretch}{1.3}
				\noindent\begin{tabular}{@{}r}
				\\
				\thepage /\pageref{LastPage} \\
			 	\footnotesize \textbf{Anexo #1 do~\footnotesize\inserirTipo~n\textordmasculine~\inserirDocNum} 
			\end{tabular}
		}
		\rfoot{\includegraphics[scale=1.2]{figuras/footImageCalibr.png}}
	}
	
	\pagestyle{anexo_sfr}
		
	\begin{center}
		{\large \textbf{ANEXO #1 - #2}}
	\end{center}
	
	
	\renewcommand{\thefigure}{#1.\arabic{figure}}
	\renewcommand{\thetable}{#1.\arabic{table}}
	\setcounter{figure}{0}
	\setcounter{table}{0}
	}
