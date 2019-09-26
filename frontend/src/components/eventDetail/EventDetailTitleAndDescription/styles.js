import styled from 'styled-components'

// lib
import { COLORS } from '../../../lib/styles'

export const Title = styled.h2`
  font-size: 33px;
  font-family: Comfortaa;
  font-weight: bold;
  color: ${({ isUpcoming }) => isUpcoming ? COLORS.violetCard : COLORS.pastGrey};
`

export const Description = styled.p`
  color: ${COLORS.description};
  font-size: 14px;
  font-family: Comfortaa;
  font-weight: bold;
`