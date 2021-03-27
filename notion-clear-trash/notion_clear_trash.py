from notion.client import NotionClient

def get_trash(client):
    query = {'type':'BlocksInSpace',
             'query':'',
             'filters':
                {'isDeletedOnly':True,
                 'excludeTemplates':False,
                 'isNavigableOnly':True,
                 'requireEditPermissions':False,
                 'ancestors':[],
                 'createdBy':[],
                 'editedBy':[],
                 'lastEditedTime':{},
                 'createdTime':{}},
             'sort':'Relevance',
             'limit':1000,
             'spaceId':client.current_space.id,
             'source':'trash'}
    results = client.post('/api/v3/search', query)
    block_ids = results.json()['results']

    return block_ids

def delete_permanently(client, block_ids):
    for block_id in block_ids:
        client.post('/api/v3/deleteBlocks', {'blockIds': [block_id['id']], 'permanentlyDelete': True})

if __name__== "__main__":
    client = NotionClient(token_v2='b9cfc6a0cb46a70fe996522e0f81573ec583b76791812ee1a523b245cac4f8aa83f9dd3409b63a588ce107c23cae11f05b07790a7ff83140e0533fd67767cb4c80246d616914768265aeeb6d2db9')

    block_ids = get_trash(client)
    delete_permanently(client, block_ids)
    
    print('Successfully cleared all trash blocks.')