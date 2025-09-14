def imovel_links(imovel):
    imovel_id = imovel['id'] if isinstance(imovel, dict) else imovel.id
    return [
        {"rel": "self", "href": f"/imoveis/{imovel_id}"},
        {"rel": "update", "href": f"/imoveis/{imovel_id}", "method": "PUT"},
        {"rel": "delete", "href": f"/imoveis/{imovel_id}", "method": "DELETE"},
        {"rel": "collection", "href": "/imoveis", "method": "GET"},
    ]
