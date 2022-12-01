filetype on
filetype plugin on
filetype indent on
syntax on
set mouse=a
set showmode
set showmatch
set number
set nowrap
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
