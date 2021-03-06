import React from 'react';
import Slider from 'react-slick';

// proptypes
import { func, number } from 'prop-types';

//types
import { eventType } from '../../../lib/types';

// material ui
import Grid from '@material-ui/core/Grid';
import Hidden from '@material-ui/core/Hidden';

// styles
import { Container, SliderContainer } from './styles';

// components
import CustomArrow from '../../common/eventDetails/CustomArrow';
import CustomSlide from '../../common/eventDetails/CustomSlide';

const EventDetailSlider = ({ event, onPhotoClick, onChangeIndex, indexOfSelectedPhoto }) => {
  const sliderSettings = {
    dots: false,
    infinite: false,
    slidesToShow: 5,
    slidesToScroll: 1,
    adaptiveHeight: true,
    variableWidth: true,
    nextArrow: <CustomArrow isNextArrow />,
    prevArrow: <CustomArrow />,
    afterChange: () => onChangeIndex(indexOfSelectedPhoto + 1),
    beforeChange: (current, next) => onChangeIndex(next),
    responsive: [
      {
        breakpoint: 1280,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 1,
          adaptiveHeight: true,
        },
      },
      {
        breakpoint: 1030,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          adaptiveHeight: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          adaptiveHeight: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          adaptiveHeight: true,
        },
      },
    ],
  };

  return (
    <Container container direction="row">
      <Hidden only={['xs', 'sm']}>
        <Grid item md={1} />
      </Hidden>
      <SliderContainer item md={10}>
        <Slider {...sliderSettings}>
          {event.photos &&
            event.photos.map((photo, index) => (
              <CustomSlide key={`photo_${photo.url}`} onPhotoClick={onPhotoClick} photo={photo} index={index} />
            ))}
        </Slider>
      </SliderContainer>
      <Hidden only={['xs', 'sm']}>
        <Grid item md={1} />
      </Hidden>
    </Container>
  );
};

EventDetailSlider.propTypes = {
  event: eventType.isRequired,
  onPhotoClick: func.isRequired,
  onChangeIndex: func.isRequired,
  indexOfSelectedPhoto: number.isRequired,
};

export default EventDetailSlider;
