# i* Strategic Rationale Model

## Purpose

The Strategic Rationale model looks at each actor and shows what they want to achieve and what they need to do. It identifies their goals, tasks and resources, and shows how these elements contribute to one another.

This model is based on the two main functions currently described in the group plan:

- Customer multi-vendor ordering and checkout
- Producer fulfilment and the weekly settlement

## Main actors and their rationale

### Customer

**Goals**
  - Buy products from local producers
  - Receive the correct items

**Desires**
  - Have a clear ordering experience
  - Receive reliable order updates

**Tasks**
  - Browse products
  - Check product availability
  - Create a basket
  - Complete checkout
  - Review order updates

**Resources**
  - Product details
  - Prices and availability information
  - Order information

### BRFN Marketplace

**Goals**
  - Coordinate multi-vendor orders
  - Support producer fulfilment
  - Keep accurate payment and settlement records

**Desires**
  - Reliable order processing
  - Accurate financial records
  - Clear communication between customers and producers

**Tasks**
  - Validate customer baskets
  - Split orders between producers
  - Check the 48hour preparation lead time
  - Send order requests to producers
  - Process producer responses
  - Coordinate customer payments
  - Calculate the 5% commission
  - Coordinate weekly settlements

**Resources**
  - Customer orders
  - Producer details and product availability
  - Producer responses
  - Payment results
  - Fulfilment and settlement records

### Producer

**Goals**
  - Receive and fuflil orders
  - Get paid accurately
  - Keep product listings up to date

**Desires**
  - Receive clear order and fulfilment information
  - Receive reliable settlement details

**Tasks**
  - Update product information and availability
  - Respond to order requests
  - Accept, partially accept or reject sub-orders
  - Prepare accepted orders
  - Arrange delivery or collection
  - Review weekly statements

**Resources**
  - Product and stock information
  - Order details
  - Settlement information

### Payment Service

**Goals**
  - Process customer payments
  - Process producer payouts

**Desires**
  - Reliable transaction processing
  - Accurate transaction results

**Tasks**
  - Receive payment requests
  - Process transactions
  - Return success or failure results
  - Process payout requests

**Resources**
  - Payment and payout requests
  - Transaction results
  - Payout details

### BRFN Administrator

**Goals**
  - Help keep the marketplace running
  - Resolve operational problems

 **Desires**
  - Keep records accurate
  - Deal with issues effectively

**Tasks**
  - Investigate producer not responding
  - Handle disputes
  - Investigate fulfilment problems
  - Look into settlement issues

**Resources**
  - Order records
  - Producer details
  - Dispute information
  - Settlement records

**## How relationships are used in the SR model**

The SR model uses different relationships to show how each actor works towards their goals. Decomposition is used to break down a larger task or goal into smaller parts. For example, completing checkout involves creating a basket, checking product availability and confirming the order. Relationships to show how a task helps achieve a goal. For example, splitting orders between producers helps the marketplace coordinate multi-vendor orders. Contribution relationships show how a task or resource helps achieve a desired outcome. For example, sending clear order notifications helps improve communication between the marketplace and producers.

These relationships help show how each actor's tasks and resources support their goals and desires.

**## Consistency with the other models**

The SR model should match the other models created by the group. The Strategic Dependency model shows which actors depend on each other and what they need, while the Strategic Rationale model looks at each actor's goals, tasks and resources in more detail. The Strategic BPMN model gives an overview of the business processes and responsibilities, and the Operational BPMN models show the detailed steps, decisions and interactions involved in those processes. The Camunda workflows are then used to implement the agreed processes.

If a responsibility or process changes in one of the other models, we should check whether the SR model also needs updating. This will help keep the models consistent as the project develops.

## simple diagram displaying this (needs doing  ! !)
