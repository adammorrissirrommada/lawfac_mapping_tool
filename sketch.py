## GENERIC KEYWORD SEARCH CLASSES, NOT SPECIFIC TO LAW PROJECT
class keyword:
    # Class to hold the values and options for a single keyword
    def __init__(self, value, weight=1.0, allow_synonyms = False):
        w = self
        w.value = value                 # [string] The actual word for this instance
        w.weight = 1.0                  # [float] The relative importance of this word, used for scoring relevance in mapping
        w.synonyms = []                 # [list] List of synonyms for this word
        if allow_synonyms:
            w.synonyms = []             # TODO: populate this automatically using an external library.
    
    def find_in_text(self, text_to_search):
        #  How many times does this word (or any synonym, if requested) occur in the provided text string ?
        count, position = [],[] #TODO [do the search]
        
        return count, position 

class keyword_group:
    # Class to hold a group of keywords and rules for how the score should be calculated
    # e.g.  simply a boolean if any are present?
    #       weighted sum?
    def __init__(self, keywords=None):

        self.keywords = dict() # Dictionary storing the keyword objects, using the word itself as key

        if keywords:
            for k in keywords:
                self.add(k)

    def add(self, keyw):
        # Add a keyword to this item
        self.keywords[keyw.value] = keyw

    def search_and_score(self, text_to_search):
        # Function to search arbitrary text for the keywords in the group and score for relevance
        score = []
        #score = titus_tool(text_to_search)
        return score

## UNIQUE TO LAW PROJECT            
class mapping_item(keyword_group):
    # Derived class to additionally hold info about a single item in the mapping
    # - item label/text/header
    # - a set of keywords
    def __init__(self, item_header, keywords):
        g = self
        g.header_text = item_header
        g.keywords = keyword_group(keywords)

class mapping_guide:
    def __init__(self, spreadsheet):
        m = self
        
        # A mapping guide is a list of mapping_items
        m.items = []

        # Load the items and keywords etc. from the Excel spreahdsheet mapping guide (or whatever source).
        # Each output is a [1 x N_ITEMS] list
        item_headers, item_keywords, weights, allow_synonyms = [],[],[],[] #TODO Create a load tool that returns these args

        # Create the objects for each item in the guide
        for hdr in item_headers:
            kw_list = []
            for word, wts, allow_syn in zip(item_keywords,weights,allow_synonyms):
                # Create a new keyword object
                cur_keyword = keyword(word, wts, allow_syn)
                kw_list.append(cur_keyword)

            # Create a new mapping item using the keyword objects 
            cur_item = mapping_item(hdr, kw_list)   
            m.items.append(cur_item)

# Load the case text

# Extract variables (e.g. dates, participants, court IDs etc.)

# Clean, tokenize etc.

# Load the mapping guide
mg = mapping_guide([])

# Perform mapping (fully auto or with manual intervention, gui etc.)

# Output results