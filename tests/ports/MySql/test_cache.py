import unittest

from app.ports.MySql.cache import Cache

class CacheTest(unittest.TestCase):
    
    def test_cache_method(self) : 
        cache = Cache()
        
        candidates = [{"first_name" : "John", "last_name":"Doe", "party" : "Love"}, {"first_name" : "Jane", "last_name":"Doe", "party": "War"}]
        cache.add_datas(candidates, "candidates")
        
        datas_cache = cache.get_datas("candidates")
        self.assertEqual(candidates, datas_cache)
        self.assertEqual(2, len(datas_cache))
        
        
    def test_check_datas_cached(self) :
        cache = Cache()
        
        candidates = [{"first_name" : "John", "last_name":"Doe", "party" : "Love"}, {"first_name" : "Jane", "last_name":"Doe", "party": "War"}]
        cache.add_datas(candidates, "candidates")
        
        self.assertTrue(cache.is_datas_cached("candidates"))
        self.assertFalse(cache.is_datas_cached("deputies"))
        self.assertFalse(cache.is_datas_cached("candidate"))
        
        
    def test_singleton_implemented_in_cache(self) :
        cache_first = Cache()
        candidates = [{"first_name" : "John", "last_name":"Doe", "party" : "Love"}, {"first_name" : "Jane", "last_name":"Doe", "party": "War"}]
        cache_first.add_datas(candidates, "candidates")
        
        cache_second = Cache()
        candidates_get_from_second_cache = cache_second.get_datas("candidates")
        
        self.assertEqual(2, len(candidates_get_from_second_cache))
        self.assertEqual([{"first_name" : "John", "last_name":"Doe", "party" : "Love"}, {"first_name" : "Jane", "last_name":"Doe", "party": "War"}], candidates_get_from_second_cache)
        