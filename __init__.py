class MaxDmgLoader():
    from .app.Loader    import Loader, alter_schema

    def __init__(self, schema=None):
        if schema:
            MaxDmgLoader.alter_schema(schema)

    def Load(self,
             AIRTABLE_API_KEY, 
             AIRTABLE_BASE_ID,
             AIRTABLE_STATES_TABLE_ID,
             AIRTABLE_STATES_TABLE_VIEW_ID,
             AIRTABLE_TRANSITIONS_TABLE_ID,
             AIRTABLE_TRANSITION_TABLE_VIEW_ID,
             AIRTABLE_FORMS_TABLE_ID,
             AIRTABLE_FORMS_TABLE_VIEW_ID,
             AIRTABLE_CONFIG_TABLE_ID,
             AIRTABLE_CONFIG_TABLE_VIEW_ID
        ):
        loader = MaxDmgLoader.Loader()
        loader.load(
             AIRTABLE_API_KEY, 
             AIRTABLE_BASE_ID,
             AIRTABLE_STATES_TABLE_ID,
             AIRTABLE_STATES_TABLE_VIEW_ID,
             AIRTABLE_TRANSITIONS_TABLE_ID,
             AIRTABLE_TRANSITION_TABLE_VIEW_ID,
             AIRTABLE_FORMS_TABLE_ID,
             AIRTABLE_FORMS_TABLE_VIEW_ID,
             AIRTABLE_CONFIG_TABLE_ID,
             AIRTABLE_CONFIG_TABLE_VIEW_ID
        ) 

        return {
            'graph'         : loader.graph,
            'forms'         : loader.forms,
            'docs'          : loader.docs
        }

    def LoadFromConfig(self, config):
        return self.Load(**(vars(config)))

