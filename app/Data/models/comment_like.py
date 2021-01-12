from sqlalchemy.orm import relationship
from app.Data.db import Base
import sqlalchemy as sa


class CommentLike(Base):
    __tablename__ = 'comment_like'

    UserId = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.Id'),
        primary_key=True,
        nullable=False)
    CommentId = sa.Column(
        sa.Integer,
        sa.ForeignKey('comment.Id'),
        primary_key=True,
        nullable=False)
    Liked = sa.Column(
        sa.Boolean,
        nullable=False)

    comment = relationship('Comment', back_populates='comment_like')
    user = relationship('Comment', back_populates='comment_like')


if __name__ == "__main__":
    comment_like = CommentLike()
