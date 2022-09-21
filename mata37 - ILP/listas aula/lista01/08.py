desconto = 0.6
valor_livro = 20
custo_envio = 3
custo_envio_copia_adicional = 0.75
total_livros = 60
print("Custo total: R$", ((desconto*valor_livro+custo_envio)+(desconto*valor_livro+(custo_envio_copia_adicional*(total_livros-1)))))
