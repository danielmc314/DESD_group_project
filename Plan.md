Index:

[Sprint 0](#Sprint-0)
[Sprint 1](#Sprint-1)

## Sprint 0
### Communication channels

Whatsapp group and Github repo established
### Roles and responsibilities

Wayne: 
Zay:
Dan:
John
### 2 major functionalities

#### In scope:
###### Producer end: 
Producers require an intuitive way to upload their products etc. so we will provide a clean and simple UI where they can upload, delete and update their products with descriptions and all requirements in the case study including a way to track transaction history with a revenue summary. Requirements in the case study:

"
The technical capabilities amongst producers vary considerably across the network. Some  
operate exclusively through email and telephone-based ordering systems, dedicating  
approximately fifteen hours per week to customer communication activities. Others maintain  
basic social media presence but lack advanced technical expertise or resources for  
sophisticated digital solutions.  
All producers require intuitive mechanisms to list their products with essential information,  
specifically: product names, detailed descriptions, pricing information, and availability  
timeframes. The system must accommodate frequent seasonal inventory updates without  
requiring extensive technical knowledge or training. Producers need comprehensive visibility of
incoming orders with adequate lead time (minimum 48 hours) to prepare products  
appropriately.  
Financial requirements include weekly payment settlements with transparent audit trails  
suitable for tax reporting purposes and business accounting needs.  
"
##### Customer end: 
Customers require a categorised app like uber eats with a search system. The requirements in the case study:

"
Customers require robust product browsing capabilities organised by clearly defined categories  
including vegetables, dairy products, bakery goods, preserves, and seasonal specialities. The  
system must incorporate search functionality enabling users to locate specific items efficiently.  
The shopping experience should reflect the unique requirements of local food systems,  
including the display of harvest dates, farm origin information, and seasonal availability  
indicators. The checkout process must handle both single-vendor and multi-vendor orders  
seamlessly whilst maintaining clear communication about individual supplier responsibilities,  
delivery arrangements, and collection procedures.  
"
#### Out of scope:
##### Producer end:
We can provide an additional functionality so that producers can import their existing CSV files into the program, automatically listing their stock. We could also integrate links for their social media.

##### Customer end:
We can provide personalised recommendations based on a recommendation algorithm such as item-based collaborative filtering. It is basically 'Customers who bought X also bought Y'. Also a review and rating page for each shop and products.



### Project methodology 

#### Scrum

- **Product Owner:** Manages the Product Backlog, defines features, and prioritizes work based on business value.
- **Scrum Master:** Facilitates the Scrum process, coaches the team, and removes operational blockers.
- **Developers (Scrum Team):** A cross-functional group of members accountable for turning work into a usable product increment.

But for this project we should be all of the roles.

### Stakeholder analysis


| Stakeholder                            | Needs                                              | Priority |
| -------------------------------------- | -------------------------------------------------- | -------- |
| Producers                              | Easy listing, 48h order visibility, weekly payouts | High     |
| Individual customers                   | Browse, search, simple checkout                    | Low      |
| Community groups                       | Reliable bulk/repeat supply                        | Med      |
| Restaurants/cafes                      | Less admin across multiple suppliers               | Med      |
| Bristol Regional Food Network (client) | 5% commission, reporting, food safety              | High     |

Customers are lowest priority because community groups and restaurants, we assume, will produce more consistent, higher revenue. 

### Initial Product backlog

#### 1. Accounts & access

|ID|Item|Priority|
|---|---|---|
|ACC-01|Registration for customers and producers|Must|
|ACC-02|Login, logout and password reset|Must|
|ACC-03|Role-based access: customer, producer, admin|Must|
|ACC-04|Producer profile: farm name, address/postcode, contact, farm story|Must|
|ACC-05|Customer profile: delivery address, postcode, saved details|Should|
|ACC-06|Customer account types: individual, community group, restaurant|Could|

#### 2. Product catalogue (producer side)

| ID     | Item                                                                      | Priority |
| ------ | ------------------------------------------------------------------------- | -------- |
| CAT-01 | Create, edit and delete product listings (name, description, price, unit) | Must     |
| CAT-02 | Assign each product to a category                                         | Must     |
| CAT-03 | Set availability window (available from / to dates)                       | Must     |
| CAT-04 | Stock quantity tracking, reduced automatically on order                   | Must     |
| CAT-05 | Quick in-stock / out-of-stock toggle                                      | Should   |
| CAT-06 | Product image upload                                                      | Should   |
| CAT-07 | Harvest date field shown to customers                                     | Should   |
| CAT-08 | Duplicate a previous season's listing to relist quickly                   | Could    |

#### 3. Browsing & search (customer side)

|ID|Item|Priority|
|---|---|---|
|BRW-01|Browse by category: vegetables, dairy, bakery, preserves, seasonal specialities|Must|
|BRW-02|Keyword search across product names and descriptions|Must|
|BRW-03|Product detail page: price, producer, farm origin, harvest date|Must|
|BRW-04|Hide products outside their availability window|Must|
|BRW-05|Filters: organic, allergen-free, in season|Should|
|BRW-06|Producer page listing all their products and farm story|Should|
|BRW-07|Personalised recommendations (item-based CF with content fallback)|Could|

#### 4. Multi-vendor ordering

|ID|Item|Priority|
|---|---|---|
|ORD-01|Shopping basket holding items from multiple producers|Must|
|ORD-02|Split each order into one sub-order per producer|Must|
|ORD-03|Enforce minimum 48-hour lead time on fulfilment date|Must|
|ORD-04|Producer order dashboard showing incoming sub-orders|Must|
|ORD-05|Sub-order status flow: pending, confirmed, ready, completed|Must|
|ORD-06|Delivery or collection option chosen per producer|Should|
|ORD-07|Checkout summary showing which producer supplies what|Should|
|ORD-08|Customer order history|Should|

#### 5. Payments & settlements

All payment items use a test environment only (e.g. Stripe test mode), as the brief requires.

| ID     | Item                                                                           | Priority     |
| ------ | ------------------------------------------------------------------------------ | ------------ |
| PAY-01 | Single checkout payment for single- and multi-vendor orders (Stripe test mode) | Must         |
| PAY-02 | Automatic 5% network commission per sub-order                                  | Must         |
| PAY-03 | Record producer payout amount per sub-order                                    | Must         |
| PAY-04 | Weekly settlement batch per producer                                           | Must         |
| PAY-05 | Producer payment statement with audit trail, downloadable as CSV               | Should       |
| PAY-06 | Payment confirmation shown and emailed to customer                             | Should       |
| PAY-07 | Refunds and cancellations                                                      | Nice to have |

#### 6. Network admin

|ID|Item|Priority|
|---|---|---|
|ADM-01|Approve, suspend and manage producer accounts|Must|
|ADM-02|View all orders across the network|Must|
|ADM-03|Commission report by week and by producer|Should|
|ADM-04|Review and confirm weekly settlements before release|Should|
|ADM-05|Manage product categories|Should|
|ADM-06|Network-wide sustainability report (food miles, surplus sold)|Could|

#### 7. Traceability & food safety

|ID|Item|Priority|
|---|---|---|
|TRC-01|Allergen warnings on each product|Must|
|TRC-02|Organic certification flag on each product|Should|
|TRC-03|Best-before date on each product|Should|
|TRC-04|Link every order item to customer, product and producer records|Should|
|TRC-05|Admin lookup of all customers who bought a given product, to contact them about a quality issue|Could|

#### 8. Sustainability & community

|ID|Item|Priority|
|---|---|---|
|SUS-01|Food miles per order from customer and producer postcodes|Should|
|SUS-02|Surplus produce flag with last-minute discount price and expiry|Should|
|SUS-03|Surplus deals page for customers|Could|
|SUS-04|Producers post seasonal recipes linked to their products|Could|
|SUS-05|Producers post storage guidance per product|Could|
|SUS-06|Notify customers when new surplus is listed|Could|

#### 9. Technical & non-functional

| ID     | Item                                                                           | Priority |
| ------ | ------------------------------------------------------------------------------ | -------- |
| TEC-01 | Project setup: framework, database, repo structure, branching strategy         | Must     |
| TEC-02 | Database schema for users, products, orders, sub-orders, payments, settlements | Must     |
| TEC-03 | Docker setup so every member runs the same environment                         | Must     |
| TEC-04 | Seed data: sample producers, products and orders for demo and testing          | Must     |
| TEC-05 | Automated tests for commission, order splitting and lead-time rules            | Must     |
| TEC-06 | GDPR basics: privacy notice, secure password storage, minimal personal data    | Should   |
| TEC-07 | Responsive layout for mobile and desktop                                       | Should   |




## Sprint 1

### BPMN diagram (needs to be done)
### 2 major functionalities (Wayne)

### In scope:
#### Customer multi-vendor ordering and checkout.
1. Place order (customer user task): items from several producers, with delivery or collection chosen per producer. Submitted to the marketplace as a message.
2. Validate basket (service task): checks stock and availability windows.
3. Split order and check lead time (DMN): one sub-order per producer, each slot at least 48h away.
4. Send order to producer (parallel multi-instance sub-process): each producer does Validate order request (user task) to accept, part-accept or reject.
5. Process result (service task): re-totals and works out delivery fees. Gateway Is order possible? If no producer accepted, the order is cancelled.
6. Send result to customer: one summary showing each supplier's items, collection or delivery details, and contact.
7. Fill out payment info (customer user task), then Process payment (service task calling the payment provider).
8. Payment approved? (gateway). If yes, confirm to the customer and send Order confirmed to each producer in parallel. This message starts F2.
9. End: order confirmed.
   
##### Main exceptions:

• Item unavailable: the customer amends the basket and it's validated again.
• Slot under 48h: the customer picks a new date.
• Producer doesn't reply in 24h (timer): that sub-order is dropped and admin is told.
• Payment fails: up to 3 retries, then cancel and tell the producers.
• Customer doesn't pay within 30 minutes (timer): order withdrawn and the producers are told.

#### Producer fulfilment and weekly settlement.
##### Part A: fulfilment
1. Notify producer (service task): the order appears in their incoming orders.
2. Prepare order (producer user task), with a reminder timer 24h before the slot.
3. Shortage? (gateway): if yes, a partial refund through the payment provider.
4. Delivery or collection? (gateway), leading to Mark dispatched or Mark collected (user task).
5. Wait 48h for a problem report (event-based gateway). A report goes to Handle dispute (admin).
6. Write ledger entry (service task), which is the audit trail. End.
##### Part B: weekly settlement (timer, every Monday)
1. Collect last week's fulfilled sub-orders per producer (service task).
2. Open disputes? (gateway): disputed amounts are held until next week.
3. Calculate commission (DMN), giving the net payout.
4. Generate statement (service task): a CSV or PDF suitable for tax records.
5. Send payout (service task calling the payment provider), then email the statement. End.
##### Main exceptions
• Producer hasn't prepared by the slot: escalated to admin, who can cancel and refund.
• Customer no-show at collection (timer): admin decides.
• Payout fails: retry, then the producer updates their bank details.

### Out of scope:
An option for producers to import their existing CSV files into the program, automatically listing their stock. We could also integrate links for their social media.
Incoming orders can be coloured green, yellow or red. Green if <24 hours, Yellow if 24 > 48 and red if exceeding 48 hours.
Recommendations based on a recommendation algorithm such as item-based collaborative filtering. It is basically 'Customers who bought X also bought Y'. Also a review and rating page for each shop and products. Order history.

### Use Case 2 - Analysis of major business processes and organisational processes (2nd draft john)

The BRFN marketplace has several main business processes that need to work together to connect local food producers with customers. 
The table below shows the main processes we have identified so far, who is involved and what they are responsible for. 
This is an initial analysis and may change as we develop the project further.


| Business process | Main people involved | Main responsibilities |
|---|---|---|
| Producer and account management | Producers, BRFN administrators | Manage producer accounts and keep producer information up to date |
| Product and inventory management | Producers, marketplace | Add and update products, prices, stock levels, and seasonal availability |
| Customer browsing and ordering | Customers, marketplace, producers | Allow customers to search for products, view product information and place orders |
| Order coordination and fulfilment | Customers, producers, marketplace | Organise orders containing products from different producers and make delivery or collection arrangements clear |
| Payments and settlements | Customers, marketplace, producers, payment service | Handle simulated payments, calculate the 5% commission and keep records of payments owed to producers |
| Food quality and traceability | Producers, customers, BRFN administrators | Keep important food information available and help identify affected orders if there is a food safety issue |
| Sustainability and community information | Producers, marketplace, customers | Provide features such as food-miles information, surplus produce offers and recipes or storage advice |

These processes are connected and depend on each other. 
For example, customers need accurate product and stock information before they can place an order. 
Once an order is placed, the marketplace needs to organise the order between the relevant producers and handle the payment. 
Keeping accurate records of products, producers and orders is also important for payment records and dealing with possible food safety issues.

#### Use Case 2 - Dependencies for Multi-Vendor Ordering

We have decided to do Use Case 2. These are the different processes that need to happen in the correct order for checkout to work properly.
First, the marketplace needs to check that the products in the customer's basket are still available and that there is enough stock.
If an item is unavailable, the customer should be told so they can change their basket before continuing.

Once the customer is happy andready to place the order, the marketplace needs to split it into separate orders for each of the producers involved.
This makes it clear which products each producer is responsible for.
The customer should also be able to see the relevant delivery or collection information before confirming the purchase.

The payment result then affects what happens next.
If the payment is successful, the order will be confirmed and the stock can be updated/ relayed to the producers.
If the payment is declined, the customer should be given the option to try again.
Otherwise the order cannot proceed and stock is not affected.

Finally, the marketplace needs to keep accurate records of the order and the producer.
These records are needed to calculate the 5% commission correctly and keep track of how much each producer is owed.
This shows how stock management, ordering, payments and producer notifications all depend on each other.

This is the initial understanding for the use case process.
We may make changes .

#### Multi-vendor Ordering Points of Failure

The backlog lists the main ordering and payment requirements, but we also need to consider how the system should respond when parts of the process fail.
These risks can be considered when developing/ finalising the operational BPMN model and test cases. Especially for situations where the process does not complete as expected.

- Payment problems. Payments may be declined or the payment service may be unavailable. The system needs to allow an appropriate method to retry the order, or a seperate path without incorrectly confirming the order.

- Order processing errors. The system could create incorrect order details or fail to notify a producer. These problems could affect the order preparation process. The solution is yet to be decided but it must resolve the issue hindering the producer or custmer as little as possible (compensation or something??).

- Incorrect financial records. Errors when calculating the 5% commission or recording producer product amounts could lead to inaccurate payment records. The calculations and stored amounts should be checked through testing. If wrong, this may cause issues down the line when an eventual refund/ reimbursment happens.

#### Checking the Consistency Across Models

Our group should regularly check that our models, requirements and implementation stay consistent as the project develops.
Although each part serves a different purpose, they should all ultimately describe thesame overall process and agreed system behaviour.

We can do this by reviewing the different parts of our work together in our meetings at key stages, then recording any differences we find.
If we identify any inconsistencies, we can discuss them as a group, agree on who has the correct approach and record any changes that need to be made.
This will help us keep track of decisions, avoid conflicting versions and wasted work/time.

### Group Initial product backlog and sprint plan

We will develop the BRFN marketplace in stages following the sprint time periods. 
The aim is to agree on the main requirements first, then model the business processes before moving on to implementation and testing. 
This way everything will be discussed and agreed upon on between each sprint. 
The sprints are specified in the project assessment brief.

| Sprint        | Main focus                                        | Expected outcome                                                                                                                                                 |
| ------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sprint 0      | Group setup and initial planning                  | Set up the repository, review the case study, identify stakeholders and create an initial product backlog                                                        |
| Sprint 1: 20% | Strategic analysis and project setup              | Complete the strategic BPMN model, analyse the major business processes, agree on the two candidate functionalities with the module team, and refine the backlog |
| Sprint 2: 30% | Detailed process modelling and initial automation | Develop the two i* models, create detailed operational BPMN models for the agreed functionalities, and begin implementing the processes in Camunda               |
| Sprint 3: 50% | Implementation, integration and demonstration     | Complete and test the executable processes, connect the relevant components, handle alternative and error paths, and prepare the final demonstration             |

#### Dependencies and Risks

Some features depend on other parts of the system working correctly. 
For example, the ordering process depends on accurate product availability and stock information. 
Payment processing also needs to be linked to order confirmation, while the commission calculation must use the correct order amounts.

We should agree on the scope of the two major functionalities before developing their detailed process models. 
We also need to keep payments in a test environment, as required by the case study and assessment brief. 
Regular meetings, clear task ownership and updates to the shared repository will help the group track progress and identify problems early.

### Effective use of the GitHub/GitLab repository

Requirements:
- A proper **README**: project name, team, setup instructions
- A sensible **folder structure** (e.g. `/docs`, `/src`)
- **Branches and pull requests**, rather than everyone pushing to `main`
- **Issues** or a project board linked to backlog items
- Sprint 1 documents committed, such as the BPMN export, analysis and backlog

### Clear evidence of group activity and contribution

Requirements:
- **Stand-up notes** (date, attendees, what each person did, what's next, blockers)
- **Commits from every member's own GitHub account.** Set your Git identity properly, as covered earlier, or your commits won't show under your name
- **Meeting minutes** with decisions and actions
- A simple **contribution table**:
