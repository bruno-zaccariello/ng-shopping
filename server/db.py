import classes as cl

PRODUTOS = [
    cl.Produto(1, 'Batata', 12, 'Gostosinha'),
    cl.Produto(2, 'Abacate', 15, 'Gostosinha'),
    cl.Produto(3, 'File', 11, 'Gostosinha'),
    cl.Produto(4, 'Arroz', 20, 'Gostosinha'),
    cl.Produto(5, 'Feijao', 22, 'Gostosinha'),
    cl.Produto(6, 'Pina', 2, 'Gostosinha'),
    cl.Produto(7, 'Abacaxi', 5, 'Gostosinha'),
    cl.Produto(8, 'Alface', 3, 'Gostosinha'),
    cl.Produto(9, 'Couve Flor', 15, 'Gostosinha'),
    cl.Produto(10, 'Feijao Branco', 11, 'Gostosinha'),
    cl.Produto(11, 'Cansaco', 30, 'Gostosinha'),
    cl.Produto(12, 'Obb', 22, 'Gostosinha'),
]

USER_ADMIN = cl.User('admin', 'admin', 'Admin')
USERS = {
    USER_ADMIN.login: USER_ADMIN,
}

TOKENS = {
    
}