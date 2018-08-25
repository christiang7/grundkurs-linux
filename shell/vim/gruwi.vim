set background=dark
highlight Normal  ctermbg=NONE
highlight nonText ctermbg=NONE

hi clear
if exists("syntax_on")
   syntax reset
endif

let colors_name = "gruwi"

hi Normal		ctermfg=gray    ctermbg=black
hi Scrollbar  	ctermfg=blue    cterm=none  ctermbg=black term=none
hi Menu		  	guifg=black guibg=cyan
hi SpecialKey  	term=bold       cterm=bold  ctermfg=darkred
hi NonText	  	term=bold       cterm=bold  ctermfg=brown
hi Directory  	term=bold       cterm=bold  ctermfg=brown  
hi ErrorMsg	  	term=standout   cterm=bold  ctermfg=grey  ctermbg=red  
hi Search	  	ctermfg=white   ctermbg=darkblue 
hi MoreMsg	  	term=bold       cterm=bold  ctermfg=darkgreen	
hi ModeMsg	  	term=bold       cterm=bold  
hi LineNr	  	term=underline  cterm=bold  ctermfg=yellow
hi Question	  	term=standout   cterm=bold  ctermfg=darkgreen	
hi StatusLine	term=standout   cterm=bold,reverse ctermfg=darkblue ctermbg=white 
hi Title	  	term=bold       cterm=bold  ctermfg=green  
hi Visual	  	term=reverse	cterm=reverse  
hi WarningMsg  	term=standout   cterm=bold  ctermfg=darkred 
hi Cursor	  	ctermfg=black   ctermbg=yellow
hi Comment	  	cterm=bold      ctermfg=blue  
hi Constant	  	term=underline  cterm=bold ctermfg=magenta  
hi Special	  	term=bold       cterm=bold ctermfg=blue
hi Identifier  	term=underline  ctermfg=cyan  
hi Function  	term=bold       cterm=bold ctermfg=magenta
hi Statement  	term=bold       cterm=bold ctermfg=yellow	
hi PreProc	 	term=underline  cterm=bold ctermfg=blue   
hi Type		  	term=underline  cterm=bold ctermfg=lightgreen  
hi Error	  	term=reverse	ctermfg=darkcyan  ctermbg=black  
hi Todo 	  	term=bold       cterm=bold,reverse ctermfg=black ctermbg=yellow
hi CursorLine	term=underline  
hi CursorColumn	term=underline  
hi MatchParen	term=reverse    ctermfg=blue 
hi TabLine		term=bold,reverse  cterm=bold ctermfg=lightblue ctermbg=white 
hi TabLineFill	term=bold,reverse  cterm=bold ctermfg=lightblue ctermbg=white 
hi TabLineSel	term=reverse	ctermfg=white ctermbg=lightblue 
hi rstEmphasis	term=bold,reverse  cterm=bold ctermfg=black ctermbg=white 

hi link IncSearch		Visual
hi link String			Constant
hi link Character		Constant
hi link Number			Constant
hi link Boolean			Constant
hi link Float			Number
hi link Function		Function
hi link Conditional		Statement
hi link Repeat			Statement
hi link Label			Statement
hi link Operator		Statement
hi link Keyword			Statement
hi link Exception		Statement
hi link Include			PreProc
hi link Define			PreProc
hi link Macro			PreProc
hi link PreCondit		PreProc
hi link StorageClass	Type
hi link Structure		Type
hi link Typedef			Type
hi link Tag				Special
hi link SpecialChar		Special
hi link Delimiter		Special
hi link SpecialComment	Special
hi link Debug			Special
hi link rstTodo			Todo
hi link rstCodeBlock	Special
hi link rstDirective	Keyword


