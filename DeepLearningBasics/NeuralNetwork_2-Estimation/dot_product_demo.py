def dot_product(first_vector, second_vector):
    # Remember you can only use dot product on with the same size
    assert( len(first_vector) == len(second_vector))

    vectors_size = len(first_vector)
    dot_product_result = 0

    for index in range(vectors_size):
        dot_product_result += first_vector[index] * second_vector[index]

    return dot_product_result


test_vector_one = [2, 3, 4]
test_vector_two = [5, 6, 7]

test_dot_product = dot_product(test_vector_one, test_vector_two)

print("The result of the dot product between the two test vectors is: {}".format(test_dot_product) )