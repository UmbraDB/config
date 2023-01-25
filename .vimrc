filetype indent plugin on
syntax enable
set mouse=a
set showmode
set showmatch
set number
set nowrap
let g:javascript_plugin_jsdoc = 1
let g:javascript_plugin_ngdoc = 1
let g:javascript_plugin_flow = 1
augroup javascript_folding
    au!
    au FileType javascript setlocal foldmethod=syntax
augroup END
let g:javascript_conceal_function             = "ƒ"
let g:javascript_conceal_null                 = "ø"
let g:javascript_conceal_this                 = "@"
let g:javascript_conceal_return               = "⇚"
let g:javascript_conceal_undefined            = "¿"
let g:javascript_conceal_NaN                  = "ℕ"
let g:javascript_conceal_prototype            = "¶"
let g:javascript_conceal_static               = "•"
let g:javascript_conceal_super                = "Ω"
let g:javascript_conceal_arrow_function       = "⇒"
let g:javascript_conceal_noarg_arrow_function = "🞅"
let g:javascript_conceal_underscore_arrow_function = "🞅"
autocmd Filetype html setlocal tabstop=2 shiftwidth=2 expandtab
autocmd Filetype css setlocal tabstop=2 shiftwidth=2 expandtab
set autoindent
set incsearch
set ignorecase
set hlsearch
set statusline+=\ %F\ %M\ %Y\ %R
set statusline+=%=
set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%
set laststatus=2
au VimEnter * bel terminal 
au VimEnter * 18%wincmd -
au VimEnter * wincmd p
au VimEnter * NERDTree
au VimEnter * 8 wincmd < 
au Vimenter * wincmd p

