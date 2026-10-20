

# Case 2 - Test Cases

## TC-ORD-001: Insufficient Stock

**Precondition:** Only 2 apples are available.

**Test Data:**
- Product: Apple
- Available stock: 2
- Requested quantity: 5

**Steps:**
1. Select apples.
2. Set quantity to 5.
3. Attempt to place the order.

**Expected Result:**
- The system informs the customer that stock is insufficient.
- The customer can amend the quantity.
- The order is not confirmed.

**Actual Result:** Not tested yet.

**Status:** Not Run

---

## TC-PAY-001: Payment Declined

**Precondition:** The customer has a valid order ready for payment.

**Test Data:**
- Payment result: Declined

**Steps:**
1. Create an order with available products.
2. Proceed to checkout.
3. Use the test payment service to simulate a declined payment.
4. Check the system response.

**Expected Result:**
- The customer is informed that payment was declined.
- The customer can retry payment.
- The order is not marked as successfully paid.

**Actual Result:** Not tested yet.

**Status:** Not Run
