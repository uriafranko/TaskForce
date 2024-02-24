from textwrap import dedent

from crewai import Task


class ProductPhotographerTasks:
    def product_photograph_task(self, agent, copy, product_website, product_details):
        return Task(
            description=dedent(
                f"""\
			You are working on a new campaign for a super important customer,
			and you MUST take the most amazing photo ever for an instagram post
			regarding the product, you have the following copy:
			{copy}

			This is the product you are working with: {product_website}.
			Extra details provided by the customer: {product_details}.

			Imagine what the photo you wanna take describe it in a paragraph.
			Here are some examples for you follow:
			- high tech airplane in a beautiful blue sky in a beautiful sunset super crispy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Think creatively and focus on how the image can capture the audience's
			attention. Don't show the actual product on the photo.

			Your final answer must be 3 options of photographs, each with 1 paragraph
			describing the photograph exactly like the examples provided above.
			"""  # noqa: E501
            ),
            agent=agent,
        )

    def product_review_photo(self, agent, product_website, product_details):
        return Task(
            description=dedent(
                f"""\
			Review the photos you got from the senior photographer.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying question or delegate follow up work if
			necessary to make decisions. When delegating work send the full draft
			as part of the information.

			This is the product you are working with: {product_website}.
			Extra details provided by the customer: {product_details}.

			Here are some examples on how the final photographs should look like:
			- high tech airplane in a beautiful blue sky in a beautiful sunset super crispy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Your final answer must be 3 reviewed options of photographs,
			each with 1 paragraph description following the examples provided above.
			"""  # noqa: E501
            ),
            agent=agent,
        )
