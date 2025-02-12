from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class StudyGroup(models.Model):
    class_name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name


class Event(models.Model):
    # Define choices for the event type
    EVENT_TYPE_CHOICES = [
        ('hackathon', 'Hackathon'),
        ('seminar', 'Seminar'),
        ('workshop', 'Workshop'),
        ('conference', 'Conference'),
    ]

    title = models.CharField(max_length=200, help_text="The title of the event.")
    slug = models.SlugField(unique=True, help_text="Unique URL-friendly identifier for the event.")
    description = models.TextField(blank=True, help_text="Detailed information about the event.")

    # Field to categorize the event
    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
        default='seminar',
        help_text="Type of the event."
    )

    # Timing fields
    start_time = models.DateTimeField(help_text="Date and time when the event starts.")
    end_time = models.DateTimeField(help_text="Date and time when the event ends.")
    registration_deadline = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Deadline for event registration (if applicable)."
    )

    # Location details; this can be a physical address or an online URL
    location = models.CharField(max_length=200, help_text="Event location or online meeting URL.")

    # Organizer details, which can be later linked to a User model if needed
    organizer = models.CharField(max_length=100, help_text="Name of the organizer or organizing entity.")

    # Additional optional attributes
    max_participants = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Maximum number of participants allowed."
    )

    # Automatically managed fields for record keeping
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_ongoing(self):
        """
        Returns True if the event is currently ongoing.
        """
        now = timezone.now()
        return self.start_time <= now <= self.end_time

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_time']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
