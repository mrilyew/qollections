from resources.globals import sys, random, json, consts, Path, requests

class Utils():
    def parse_args(self):
        args = sys.argv
        parsed_args = {}
        key = None
        for arg in args[1:]:
            if arg.startswith('--'):
                if key:
                    parsed_args[key] = True
                key = arg[2:]
                parsed_args[key] = True
            #elif arg.startswith('-'):
            #    if key:
            #        parsed_args[key] = True
            #    key = arg[1:]
            #    parsed_args[key] = True
            else:
                if key:
                    parsed_args[key] = arg
                    key = None
                else:
                    pass

        return parsed_args
    
    def parse_params(self, input_data):
        params = {}
        params_arr = input_data.split('&')
        for param in params_arr:
            try:
                _spl = param.split('=')
                params[_spl[0]] = _spl[1]
            except IndexError:
                pass
        
        return params
    
    def random_int(self, min, max):
        return random.randint(min, max)
    
    def parse_json(self, text):
        try:
            return json.loads(text)
        except:
            return {}
        
    def generate_temp_entity_dir(self):
        rand = self.random_int(1, 1000000) * -1
        path = Path(f'{consts['cwd']}\\storage\\collections\\{rand}')
        path.mkdir(exist_ok=True)

        return str(path)
    
    def str_to_path(self, path):
        return Path(path)

    def find_owner(self, id, profiles, groups):
        search_array = profiles
        if id < 0:
            search_array = groups
        
        for item in search_array:
            if item.get('id') == abs(int(id)):
                return item
            
        return None
    
    def fast_get_request(self, url='', user_agent=''):
        result = requests.get(url, headers={
            'User-Agent': user_agent
        })
        parsed_result = None
        if result.headers.get('content-type').index('application/json') != -1:
            parsed_result = json.loads(result.content)

        return parsed_result
    
    def proc_strtr(self, text, length = 0):
        newString = text[:length]

        return newString + ("..." if text != newString else "")
    
    def parse_entity(self, input_string):
        from db.entity import Entity
        from db.collection import Collection

        elements = input_string.split('entity')
        if len(elements) > 1 and elements[0] == "":
            entity_id = elements[1]
            return Entity.get(entity_id)
        elif 'collection' in input_string:
            collection_id = input_string.split('collection')[1]
            return Collection.get(collection_id)
        else:
            return None

utils = Utils()
