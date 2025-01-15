local lspconfig = require("lspconfig")

lspconfig.pyright.setup({})

lspconfig.ruff.setup({
	cmd = { "ruff", "server", "--preview" },
})

vim.api.nvim_create_autocmd("BufEnter", {
    pattern = "*.html",
    command = "set ft=htmldjango"
})
