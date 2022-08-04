from unittest import TestCase

from app import app, db
from models import User, DEFAULT_PROFILE_PIC

# Let's configure our app to use a different database for tests
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly_test"

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        # As you add more models later in the exercise, you'll want to delete
        # all of their records before each test just as we're doing with the
        # User model below.
        User.query.delete()

        self.client = app.test_client()

        test_user = User(
            first_name="test_first",
            last_name="test_last",
            img_url= DEFAULT_PROFILE_PIC,
        )

        second_user = User(
            first_name="test_first_two",
            last_name="test_last_two",
            img_url= DEFAULT_PROFILE_PIC,
        )

        db.session.add_all([test_user, second_user])
        db.session.commit()

        # We can hold onto our test_user's id by attaching it to self (which is
        # accessible throughout this test class). This way, we'll be able to
        # rely on this user in our tests without needing to know the numeric
        # value of their id, since it will change each time our tests are run.
        self.user_id = test_user.id

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_list_users(self):
        """Test that users are displayed in a list."""
        with self.client as c:
            resp = c.get("/users")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("test_first", html)
            self.assertIn("test_last", html)

    def test_new_user_form(self):
        """Tests that new user form is displayed."""
        with self.client as c:
            resp = c.get('users/new')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("placeholder", html)

    def test_new_user_submitted(self):
        """Tests addition of new user from new user form exists on user list."""
        with self.client as c:
            resp = c.post(
                'users/new',
                data = {
                    'first-name': 'New',
                    'last-name' : 'User',
                    'image-url': ''
                },
                follow_redirects = True)
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('New', html)

    def test_user_details(self):
        """Test that user detail page is displayed"""
        with self.client as c:
            resp = c.get(f'/users/{self.user_id}')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Delete', html)

    def test_delete_user(self):
        """Test that a deleted user does not show up on user list."""
        with self.client as c:
            resp = c.post(f'/users/{self.user_id}/delete', follow_redirects = True)
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("test_first ", html)

    #Part 2 Tests

    # def test_add_post_display(self):
    #     """Test add post form is displayed"""
    #     with self.client as c:
    #         resp = c.get(f'/users/{self.user_id}/posts/new')
    #         html = resp.get_data(as_text = True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn("Save", html)

    # def test_add_post_to_page(self):
    #     """ Test post was added to page """
    #     with self.client as c:
    #         resp = c.post(
    #                 f'/users/{self.user_id}/posts/new',
    #                 data = {
    #                     'title' : 'First',
    #                     'content' : 'Post I Have Made',
    #                     'user_id' : self.user_id
    #                 },
    #                 follow_redirects = True)
    #         html = resp.get_data(as_text = True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('First', html)

    # def test_delete_post(self):
    #     """ Test post has been deleted """
    #     with self.client as c:
    #         resp = c.post(f'/posts/{self.post_id}/delete', follow_redirects = True)
    #         html = resp.get_data(as_text = True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertNotIn("First", html)



