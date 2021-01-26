# Practice-Model
A practice model to decide on the ideal partner based on selected input parameters.

In the world of Logistics, we have to decide how we want to allocate our orders across different partners. Different partners have different requirements including different serviceable regions and the ability to collect Cash-on-delivery. Pricing also differs across partners depending on the weight break of the parcels.

This model aims to provide the ideal partner depending on the given inputs. 

Considered inputs are the weight of the parcel, the region and if Cash-on-delivery is required.
The model first filters partners based on whether Cash-on-delivery is required, followed by the region.

Thereafter, the model filters partners based on their cost. The partner with the lowest cost is chosen. 

If different partners are tied for the lowest cost, we will look at historical performance to perform a tie-break. 

If the historical performance is the same, the model will return all partners.
