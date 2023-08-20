config.load_autoconfig(False)
config.source('themes/custom.py')
config.source('searchengines.py')
config.source('qbfetch.py')

# Keymaps {{{
nmap = lambda key, cmd: config.bind(key, cmd, mode='normal')
nmap('<Ctrl-v>', 'qbfetch')
nmap('ab', 'bookmark-add')
nmap('tb', 'config-cycle -p -t statusbar.show in-mode always ')
nmap('tt', 'config-cycle -p -t tabs.show switching multiple')
nmap('so', 'config-source')
nmap('mm', 'cmd-set-text -s :bookmark-load -t')
nmap('<Ctrl-p>', 'tab-pin ;; tab-move')
nmap(';b', 'hint buttons')
nmap(';I', 'hint inputs')
nmap(';i', 'hint images run download {hint-url}')
nmap(';s', 'hint images spawn -u searchimage.py saucenao {hint-url}')
nmap('yx', 'hint images spawn -u searchimage.py yandex {hint-url}')
nmap(';d', 'hint links run download {hint-url}')
nmap('yd', 'hint links spawn -d ytdl {hint-url}')
nmap('xp', 'hint links spawn -u proxyopen')
nmap(';m', 'hint links spawn mpv --force-window=immediate {hint-url}')
nmap('mp', 'spawn mpv --force-window=immediate {url}')
nmap('yD', 'spawn -d ytdl {url}')
nmap('cn', 'spawn -u nyarss.sh')
nmap('xc', 'spawn -u proxyopen.sh')
nmap('ts', 'spawn -u translate.sh')
nmap(';x', 'spawn -u xdg_open.sh')
nmap('gl', 'spawn gdl {url}')
# }}}

# Configuration {{{ 
homepage = 'file:///home/anon/.scripts/homepage/index.html'
c.url.default_page = homepage
c.url.start_pages  = [homepage]
c.hints.selectors['buttons'] = ['label', 'button', '.button', '[role="button"]']
# c.fileselect.handler = 'external'
# c.fileselect.multiple_files.command = ['ts', '-n', 'floating_terminal', '--', 'ranger', '--choosefiles', '{}']
# c.fileselect.single_file.command = ['ts', '-n', 'floating_terminal', '--', 'ranger', '--choosefile', '{}']
c.auto_save.session = True
c.colors.webpage.bg = '#ccccac'
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.threshold.background = 205
c.colors.webpage.darkmode.threshold.text = 20
c.completion.height = '42%'
c.completion.scrollbar.padding = 5
c.completion.scrollbar.width = 10
c.content.autoplay = False
# c.content.blocking.adblock.lists += []
# c.content.headers.user_agent = ''
c.content.notifications.enabled = False
c.content.pdfjs = False
c.content.prefers_reduced_motion = True
c.content.register_protocol_handler = False
c.content.javascript.clipboard = 'access'
c.downloads.location.prompt = False
c.downloads.remove_finished = 0 # in miliseconds
c.qt.highdpi = False
c.scrolling.smooth = True
c.spellcheck.languages = ['pt-BR', 'en-US']
c.statusbar.show = 'always'
c.tabs.background = False
c.tabs.indicator.width = 0
c.tabs.show = 'multiple'
c.zoom.default = 100
# }}}
