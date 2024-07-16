#include <gtest/gtest.h>

TEST(SimpleTest, BasicAssertion) {
    ASSERT_EQ(1, 1);
    EXPECT_GT(1, 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
