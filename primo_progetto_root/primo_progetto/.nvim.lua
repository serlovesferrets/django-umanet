local lspconfig = require("lspconfig")

lspconfig.pylsp.setup({})

lspconfig.ruff.setup({
	cmd = { "ruff", "server", "--preview" },
})

lspconfig.emmet_language_server.setup({})

vim.api.nvim_create_autocmd("BufEnter", {
    pattern = "*.html",
    command = "set ft=htmldjango"
})
